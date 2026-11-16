// TAKE-HOME PROJECT: Bulletproof Bank
// After lesson C10 (Exceptions and Debugging) - about 1–2 hours, in chunks over the next few days.
//
// Upgrade your bank account into a program that handles every error properly and keeps a
// log file.
//
// Milestones (make each one work before starting the next):
//   [ ] 1. Custom exceptions: InsufficientFundsException (with the shortfall) and
//          AccountLockedException
//   [ ] 2. PIN entry: 3 wrong tries locks the account (throw AccountLockedException; catch it
//          in the menu)
//   [ ] 3. Every transaction is appended to transactions.log with the date and time
//   [ ] 4. Withdrawals and deposits validate amounts and throw ArgumentOutOfRangeException
//          for ≤ 0
//   [ ] 5. The menu catches each exception type separately with a friendly message – the
//          program never crashes
//
// Stretch: Read transactions.log back at start-up to rebuild the balance (and skip corrupt
// lines).
//
// Bring it to the next session - working or stuck, both are fine.

Console.WriteLine("Bulletproof Bank – build the menu here");

public class InsufficientFundsException : Exception
{
}

public class AccountLockedException : Exception
{
}
