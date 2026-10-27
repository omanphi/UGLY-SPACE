"""Independent finite enumeration and boundary checks for the paper's illustration."""

import math
import unittest

from toy_model import evaluate, solve_probability


def enumerate_distribution(costs, base, penalty):
    """Direct normalization for small cases, separate from the closed-form code."""
    weights = [b * math.exp(-penalty * a) for a, b in zip(costs, base)]
    return [w / sum(weights) for w in weights]


class ToyModelTests(unittest.TestCase):
    def test_closed_forms_against_finite_enumeration(self):
        for n in (1, 2, 4, 8, 16):
            for penalty in (0.0, 0.2, 0.5, 1.0):
                for ugly in (False, True):
                    with self.subTest(n=n, penalty=penalty, ugly=ugly):
                        costs = [0.0] * n + [float(n)] if ugly else [float(n)] * n + [0.0]
                        q = enumerate_distribution(costs, [1 / (n + 1)] * (n + 1), penalty)
                        result = evaluate(n, penalty, valid_is_ugly=ugly)
                        self.assertAlmostEqual(result.mean_h * q[-1], 1.0, places=12)
                        self.assertAlmostEqual(result.success_h, 1 - (1 - q[-1]) ** (n + 1), places=12)

    def test_separation_and_budget_bounds(self):
        for n in (1, 4, 8, 16, 64):
            result = evaluate(n, 0.5)
            self.assertGreaterEqual(result.ratio, 0.5 * math.exp(0.5 * n))
            self.assertGreaterEqual(result.success_m, 1 - math.exp(-1))
            self.assertLessEqual(result.success_h, 2 * math.exp(-0.5 * n))
            if n > math.log(20) / 0.5:
                self.assertLess(result.success_h, 0.1)
                self.assertGreater(result.success_m, 0.6)

    def test_pretty_valid_candidate_reverses_effect(self):
        means = [evaluate(8, penalty, valid_is_ugly=False).mean_h for penalty in (0, 0.1, 0.5, 1)]
        self.assertTrue(all(a > b for a, b in zip(means, means[1:])))

    def test_sensitivity_identity_on_nonuniform_multiple_solution_instance(self):
        costs, base, valid = [0.0, 0.2, 1.0, 1.8], [0.1, 0.2, 0.3, 0.4], (1, 3)
        penalty, step = 0.7, 1e-5
        q = enumerate_distribution(costs, base, penalty)
        success = sum(q[i] for i in valid)
        conditional = sum(q[i] * costs[i] for i in valid) / success
        overall = sum(a * b for a, b in zip(costs, q))

        def log_mean(value):
            dist = enumerate_distribution(costs, base, value)
            return -math.log(sum(dist[i] for i in valid))

        derivative = (log_mean(penalty + step) - log_mean(penalty - step)) / (2 * step)
        self.assertAlmostEqual(derivative, conditional - overall, places=9)

    def test_bounded_range_for_every_nonempty_valid_subset(self):
        costs, base = [0.1, 0.3, 0.9, 1.4], [0.1, 0.2, 0.3, 0.4]
        for penalty in (0, 0.5, 2):
            q = enumerate_distribution(costs, base, penalty)
            for mask in range(1, 1 << len(costs)):
                valid = [i for i in range(len(costs)) if mask & (1 << i)]
                ratio = sum(base[i] for i in valid) / sum(q[i] for i in valid)
                bound = penalty * (max(costs) - min(costs))
                self.assertGreaterEqual(ratio + 1e-12, math.exp(-bound))
                self.assertLessEqual(ratio, math.exp(bound) + 1e-12)

    def test_zero_penalty_and_probability_boundaries(self):
        result = evaluate(8, 0)
        self.assertAlmostEqual(result.ratio, 1)
        self.assertAlmostEqual(result.success_h, result.success_m)
        self.assertEqual(solve_probability(1, 10), 1)
        self.assertEqual(solve_probability(0, 10), 0)
        self.assertEqual(solve_probability(1, 0), 0)
        self.assertEqual(solve_probability(0.5, 2), 0.75)

    def test_all_valid_and_shift_invariance(self):
        base, costs = [0.25, 0.75], [0.2, 0.8]
        q = enumerate_distribution(costs, base, 0.6)
        shifted = enumerate_distribution([a + 10 for a in costs], base, 0.6)
        self.assertAlmostEqual(sum(q), 1)
        self.assertAlmostEqual(solve_probability(sum(q), 1), 1)
        for a, b in zip(q, shifted):
            self.assertAlmostEqual(a, b)

    def test_small_probability_avoids_cancellation(self):
        self.assertGreater(solve_probability(1e-20, 10), 0)
        self.assertAlmostEqual(solve_probability(1e-20, 10) / 1e-19, 1)

    def test_extreme_penalty_retains_logarithmic_mean(self):
        result = evaluate(100, 100)
        self.assertTrue(math.isinf(result.mean_h))
        self.assertTrue(math.isfinite(result.log_mean_h))
        self.assertEqual(result.success_h, 0)

    def test_invalid_arguments(self):
        for n in (0, -1, 1.5, True):
            with self.assertRaises(ValueError):
                evaluate(n, 0.5)
        for penalty in (-1, math.inf, math.nan):
            with self.assertRaises(ValueError):
                evaluate(4, penalty)
        for probability, budget in ((-0.1, 1), (1.1, 1), (math.nan, 1), (0.5, -1), (0.5, 1.5)):
            with self.assertRaises(ValueError):
                solve_probability(probability, budget)


if __name__ == "__main__":
    unittest.main()
