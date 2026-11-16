using System.Diagnostics;

static async Task<string> Cook(string item, int seconds)
{
    await Task.Delay(seconds * 1000);
    return item;
}
