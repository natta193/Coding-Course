// TAKE-HOME PROJECT: Unit Converter Pro
// After lesson C02 (Types, Variables and Input) - about 1–2 hours, in chunks over the next few days.
//
// A converter that can't be crashed by bad input, using C#'s types properly.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. A menu loop with at least 6 conversions: °C↔°F, km↔miles, kg↔stone, GBP→EUR/USD
//          (make up rates as const decimal)
//   [ ] 2. Read every number with TryParse – re-ask on bad input, never crash
//   [ ] 3. Use decimal for money and double for everything else – comment why
//   [ ] 4. Format output with :F2, :N0 or :C as appropriate
//   [ ] 5. Show the integer-division trap: print 7 / 2 and 7 / 2.0 with a comment explaining
//
// Stretch: Keep a history of the last 5 conversions in an array and add a "history" menu
// option.
//
// Bring it to the next session - working or stuck, both are fine.

const decimal GbpToEur = 1.17m;

Console.WriteLine("UNIT CONVERTER PRO");
