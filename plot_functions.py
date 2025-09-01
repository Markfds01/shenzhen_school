import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

def plot_well_mixed_ODES(df):
    plt.figure(figsize=(12, 6))
    plt.title("Well-Mixed ODEs Simulation")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.plot(df['Time'], df['Susceptible'], label='Susceptible', color='blue')
    plt.plot(df['Time'], df['Infected'], label='Infected', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='green')
    plt.legend()
    plt.grid()
    plt.show()

def plot_well_mixed_stochastic(df):

    plt.figure(figsize=(12, 6))
    plt.title("Well-Mixed Stochastic Simulation")
    plt.xlabel("Time")
    plt.ylabel("Population")
    for sim in df['Simulation'].unique():
        df_plot = df[df['Simulation']==sim]
        plt.scatter(df_plot['Time'], df_plot['Susceptible'], color='blue')
        plt.scatter(df_plot['Time'], df_plot['Infected'], color='red')
        plt.scatter(df_plot['Time'], df_plot['Recovered'], color='green')
    plt.legend()
    plt.grid()
    plt.show()

def plot_well_mixed_Gillespie(df):
    plt.figure(figsize=(12, 6))
    plt.title("Well-Mixed ODEs Simulation")
    plt.xlabel("Time")
    plt.ylabel("Population")
    for sim in df['Simulation'].unique():
        df_plot = df[df['Simulation']==sim]
        plt.scatter(df_plot['Time'], df_plot['Susceptible'], color='blue')
        plt.scatter(df_plot['Time'], df_plot['Infected'], color='red')
        plt.scatter(df_plot['Time'], df_plot['Recovered'], color='green')
    plt.legend()
    plt.grid()
    plt.show()

def plot_stochastic_networks(df):
    plt.figure(figsize=(12, 6))
    plt.title("Stochastic Networks Simulation")
    plt.xlabel("Time")
    plt.ylabel("Population")
    for sim in df['Simulation'].unique():
        df_plot = df[df['Simulation']==sim]
        plt.scatter(df_plot['Time'], df_plot['Susceptible'], color='blue')
        plt.scatter(df_plot['Time'], df_plot['Infected'], color='red')
        plt.scatter(df_plot['Time'], df_plot['Recovered'], color='green')
    plt.legend()
    plt.grid()
    plt.show()

def plot_networks_Gillespie(df):
    plt.figure(figsize=(12, 6))
    plt.title("Gillespie Networks Simulation")
    plt.xlabel("Time")
    plt.ylabel("Population")
    plt.plot(df['Time'], df['Susceptible'], label='Susceptible', color='blue')
    plt.plot(df['Time'], df['Infected'], label='Infected', color='red')
    plt.plot(df['Time'], df['Recovered'], label='Recovered', color='green')
    plt.legend()
    plt.grid()
    plt.show()
