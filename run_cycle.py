#!/usr/bin/env python3
"""
REPEG ATA© Oracle - Main entry point
"""

import argparse
from datetime import datetime
from engine.oracle_node import OracleNode


def main():
    parser = argparse.ArgumentParser(description="REPEG ATA© Oracle")
    parser.add_argument("--ticker", type=str, help="Specific ticker (e.g. BRENT, UNIT)")
    parser.add_argument("--continuous", action="store_true", help="Run in continuous mode")
    parser.add_argument("--interval", type=int, default=300, help="Interval in seconds")

    args = parser.parse_args()

    print("=" * 90)
    print("REPEG ATA© Oracle Node")
    print("Asset Tracking Algorithm - Secure Off-Chain Price Extrapolation")
    print("=" * 90)
    print(f"Started at: {datetime.now()}\n")

    node = OracleNode()

    if args.continuous:
        node.run_forever(interval_seconds=args.interval)
    else:
        ticker = args.ticker.upper() if args.ticker else None
        results = node.run_cycle(ticker)

        print("\n" + "=" * 90)
        print("FINAL EXTRAPOLATION RESULTS")
        print("=" * 90)
        for tkr, result in results.items():
            print(f"Ticker                  : {result['ticker']}")
            print(f"Extrapolated Price      : {result['extrapolated_price']}")
            print(f"Human Readable          : {result['extrapolated_price'] / 1e18:.8f}")
            print(f"Confidence              : {result['confidence'] / 100:.2f}%")
            print(f"Sources Used            : {len(result.get('sources_used', []))}")
            print(f"Timestamp               : {result['timestamp']}")
            print("-" * 60)


if __name__ == "__main__":
    main()