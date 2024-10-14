module stock_trading_problem;

import std::io;
import std::collections::list;

fn void main() {
	const int K = 2;
	const int[<*>] PRICES = {3,2,6,5,0,3};
	const usz DAYS = PRICES.len;

	if (K == 0 || DAYS == 0) return;

	int max_profit = 0;
	if (K >= DAYS / 2) {
		for (int i = 1; i < DAYS; ++i) {
			max_profit = max((PRICES[i] - PRICES[i - 1]), 0);
		}
	}
	io::printfn("DAYS: %d, no. of transactions: %d", DAYS, K);

	int[K + 1][DAYS + 1] dp; 

	for (usz t = 1; t <= K; ++t) {
		for (usz d = 1; d < DAYS - 1; ++d) {
			int max_price_diff = -PRICES[0];

			dp[t][d] = max(dp[t][d - 1], PRICES[d] + max_price_diff);
			max_price_diff = max(dp[t - 1][d] - PRICES[d], max_profit);
		}
	}

	// max_profit = dp[K][DAYS - 1];
	io::printfn("Max profit: %d", max_profit);
}
