from src.data_cleaning import load_data, clean_data
from src.analysis import delay_by_airline, delay_by_month, busiest_airports
from src.visualization import plot_airline_delay, plot_month_delay, plot_airport_traffic

df = load_data("data/flights.csv")

df = clean_data(df)

airline_delay = delay_by_airline(df)
month_delay = delay_by_month(df)
airport_traffic = busiest_airports(df)

plot_airline_delay(airline_delay)
plot_month_delay(month_delay)
plot_airport_traffic(airport_traffic)

print("Analysis completed. Check outputs folder.")