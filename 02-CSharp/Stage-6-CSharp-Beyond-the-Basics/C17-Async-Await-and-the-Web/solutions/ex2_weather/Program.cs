using System.Net.Http.Json;

string[] cities = { "Cambridge", "Edinburgh", "Tokyo", "Cairo", "Reykjavik" };
using var http = new HttpClient { Timeout = TimeSpan.FromSeconds(10) };

async Task<(string City, double? Temp)> GetTempAsync(string city)
{
    try
    {
        var geo = await http.GetFromJsonAsync<GeoResult>(
            $"https://geocoding-api.open-meteo.com/v1/search?name={Uri.EscapeDataString(city)}&count=1");
        var place = geo?.Results?.FirstOrDefault();
        if (place is null) return (city, null);
        var wx = await http.GetFromJsonAsync<Forecast>(
            $"https://api.open-meteo.com/v1/forecast?latitude={place.Latitude}&longitude={place.Longitude}&current=temperature_2m");
        return (city, wx?.Current.Temperature_2m);
    }
    catch (Exception ex) when (ex is HttpRequestException or TaskCanceledException)
    {
        return (city, null);
    }
}

var results = await Task.WhenAll(cities.Select(GetTempAsync));
foreach (var (city, temp) in results.OrderByDescending(r => r.Temp ?? double.MinValue))
    Console.WriteLine($"{city,-10} {(temp is null ? "unavailable" : $"{temp:F1}°C")}");

record GeoResult(List<Place>? Results);
record Place(string Name, double Latitude, double Longitude);
record Forecast(Current Current);
record Current(double Temperature_2m);
