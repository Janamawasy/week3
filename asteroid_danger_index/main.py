import config
import fetch_data
import visualization
import processing
import interface
import asyncio

def main():
    START_DATE = '2015-09-08'
    END_DATE = '2015-09-12'
    API_KEY = config.api_key

    api = f'https://api.nasa.gov/neo/rest/v1/feed?start_date={START_DATE}&end_date={END_DATE}&api_key={API_KEY}'
    data = fetch_data.fetch_data(api)
    pop_data = processing.populate_data(data)
    # fitch_data.load_data(pop_data)
    handle_main(pop_data)

async def main_parallel_api():
    month_data = await main_month()
    pop_data = processing.populate_month_data(month_data)
    # fitch_data.load_data(pop_data)
    handle_main(pop_data)

def handle_main(pop_data):
    a, b, c = interface.handle_input()
    danger_dict = processing.danger_calculator(pop_data, a, b, c)
    print(danger_dict)
    visualization.plot_tags(danger_dict, a, b, c)


async def main_month():
    API_KEY = config.api_key
    urls = [f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-08&end_date=2015-09-12&api_key={API_KEY}',
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-10-08&end_date=2015-10-12&api_key={API_KEY}',
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-11-08&end_date=2015-11-12&api_key={API_KEY}',
            f'https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-12-08&end_date=2015-12-12&api_key={API_KEY}']
    month_data = await fetch_data.fetch_month_data(urls)
    return month_data


if __name__ == '__main__':
    ''' main quastion - fetch data with single http request '''
    # main()
    ''' extra : fetch data with parallel http requests  '''
    asyncio.run(main_parallel_api())


