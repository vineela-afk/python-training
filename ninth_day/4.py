import requests
import concurrent.futures
import logging

logging.basicConfig(filename='log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_location(lat, lon):
    try:
        url = f'https://www.mapquestapi.com/geocoding/v1/reverse?key=KEY&location={lat},{lon}'
        response = requests.get(url)
        response_data = response.json()
        
        if response_data['info']['statuscode'] == 0:
            location_data = response_data['results'][0]['locations'][0]
            street = location_data.get('street', '')
            city = location_data.get('adminArea5', '')
            country = location_data.get('adminArea1', '')
            postalcode = location_data.get('postalCode', '')
            
            filename = f'{street}_{postalcode}.json'
            with open(filename, 'w') as file:
                file.write(response.text)
            logging.info(f'Parsed information of {lat},{lon} saved to {filename}')
        else:
            logging.warning(f'Failed to fetch data for {lat},{lon}: {response_data["info"]["messages"][0]}')
            
    except Exception as e:
        logging.error(f'Error occurred for {lat},{lon}: {str(e)}')

def main():
    try:
        with open('locations.txt', 'r') as file:
            locations = [line.strip().split(',') for line in file]

        with concurrent.futures.ThreadPoolExecutor() as executor:
            executor.map(lambda loc: parse_location(loc[0], loc[1]), locations)

    except FileNotFoundError:
        logging.error('File not found: locations.txt')
    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')

if __name__ == '__main__':
    main()
