int[] nums = { 5, 12, 8, 3, 12, 19 };

var big = from n in nums
          where n > 6
          orderby n descending
          select n * 10;           // same as Where/OrderBy/Select

var unique = nums.Distinct();     // 5 12 8 3 19
var pairs = new[] { "ab", "cd" }.SelectMany(s => s);   // a b c d
var lookup = nums.ToDictionary(n => n, n => n * n);      // throws on dupes!
