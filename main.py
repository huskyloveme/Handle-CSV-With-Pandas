import pandas as pd
import matplotlib.pyplot as plt

#Read data
data = pd.read_csv("Ecommerce_Purchases.csv")
#Make State column
data['State'] = data['Address'].str.split(' ').str[-2]
def option_1():
    """
    1. Find the relationship between top 5 Job designation and total Purchase amount
    """

    #List name of Top 5 Job
    list_top5_job = data['Job'].value_counts().head(5).index

    #Data of Top 5 Job
    data_top5_job = data.loc[data['Job'].isin(list_top5_job)]

    #Sum Purchase Price and Count each of Top 5 Job
    result_1 = data_top5_job.groupby('Job').agg({'Purchase Price': ['sum', 'count']}).sort_values(('Purchase Price', 'count'), ascending=False)

    #Show
    data_2D = data_top5_job.groupby('Job')['Purchase Price'].sum()
    plt.figure(figsize=(15, 5))
    plt.xlim(-1, 5)
    plt.ylim(0, 2000)
    plt.title('relationship between top 5 Job designation and total Purchase amount')
    plt.plot(data_2D.index, data_2D.values, marker='o', markersize=10, linestyle='-', color='blue', label='Large Marker')
    plt.show()

def option_2():
    """
    2. Find the relationship between Job designation and mean Purchase amount
    """
    print(data.groupby('Job').agg({'Purchase Price': ['mean']}).sort_values(('Purchase Price','mean'),ascending=False).head(10))

def option_3():
    """
    3. How does purchase value depend on the Internet Browser used and Job (Profession) of the purchaser?
    """
    print(data.groupby(['Job','Browser Info']).agg({'Purchase Price': ['mean']}).sort_values(('Purchase Price','mean'),ascending=False).head(10))
    print(data.groupby(['Job','Browser Info']).agg({'Purchase Price': ['mean']}).sort_values(('Purchase Price','mean'),ascending=True).head(10))

def option_4():
    """
    4. What are the patterns, if any, on the purchases based on Location (State) and time of purchase (AM or PM)?
    """
    print('TOP 10 State on AM ')
    print(data.groupby(['State', 'AM or PM']).agg({'Purchase Price': ['sum']})\
    .sort_values(['AM or PM',('Purchase Price', 'sum')],ascending=[True,False]).head(10))

    print('TOP 10 State on PM ')
    print(data.groupby(['State', 'AM or PM']).agg({'Purchase Price': ['sum']})\
    .sort_values(['AM or PM',('Purchase Price', 'sum')],ascending=[False,False]).head(10))

def option_5():
    """
    5. How does purchase depend on ‘CC’ provider and time of purchase ‘AM or PM’?
    """
    print(data.groupby(['CC Provider','AM or PM']).agg({'Purchase Price': ['sum','count']}).sort_values(['AM or PM',('Purchase Price','count')],ascending=[True,False]))

def option_6():
    """
    6. What are top 5 Location(State) for purchases?
    """
    print("Top 5 Purchases(SUM):")
    print(data.groupby('State').agg({'Purchase Price': ['sum']})\
    .sort_values(('Purchase Price', 'sum'),ascending=[False]).head(5))

    print("Top 5 Purchases(COUNT):")
    print(data.groupby('State').agg({'Purchase Price': ['count']})\
    .sort_values(('Purchase Price', 'count'),ascending=[False]).head(5))

if __name__ == '__main__':
    print("1. Find the relationship between top 5 Job designation and total Purchase amount")
    print("2. Find the relationship between Job designation and mean Purchase amount")
    print("3. How does purchase value depend on the Internet Browser used and Job (Profession) of the purchaser?t")
    print("4. What are the patterns, if any, on the purchases based on Location (State) and time of purchase (AM or PM)?")
    print("5. How does purchase depend on ‘CC’ provider and time of purchase ‘AM or PM’?")
    print("6. What are top 5 Location(State) for purchases?")
    while True:
        print("Choose the option: ", end='')
        n = int(input())
        eval('option_' + str(n) + '()')
