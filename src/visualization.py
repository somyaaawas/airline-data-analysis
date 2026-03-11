import matplotlib.pyplot as plt
import seaborn as sns

def plot_airline_delay(data):

    plt.figure(figsize=(10,6))
    data.plot(kind="bar")
    plt.title("Average Delay by Airline")
    plt.ylabel("Delay (minutes)")
    plt.xlabel("Airline")

    plt.tight_layout()
    plt.savefig("outputs/delay_by_airline.png")

def plot_month_delay(data):

    plt.figure(figsize=(10,6))
    sns.lineplot(x=data.index,y=data.values)

    plt.title("Average Delay by Month")
    plt.xlabel("Month")
    plt.ylabel("Delay")

    plt.tight_layout()
    plt.savefig("outputs/delay_by_month.png")

def plot_airport_traffic(data):

    plt.figure(figsize=(10,6))
    data.plot(kind="bar")

    plt.title("Top 10 Busiest Airports")

    plt.tight_layout()
    plt.savefig("outputs/airport_traffic.png")