using System.Net.Http.Json;

using var http = new HttpClient();
string url = "https://api.open-meteo.com/v1/forecast" +
             "?latitude=52.2&longitude=0.12&current=temperature_2m";

var data = await http.GetFromJsonAsync<Forecast>(url);
Console.WriteLine($"Cambridge: {data?.Current.Temperature_2m}°C");

record Forecast(Current Current);
record Current(double Temperature_2m);
