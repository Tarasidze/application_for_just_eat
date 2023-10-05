# Python Just-eat Class

 This class provides the possibility to get all restaurants by zip code

## :memo: Table of Contents

- [Installation](#rocket-getting-started)
- [API usage](#computer-api-usage)

## :rocket: Installation 

1. **Clone the repository**:

   ```
   git clone https://github.com/Tarasidze/application_for_just_eat.git   
   
   ```  
2. **Install requirements**

   ```
   pip install requirements.txt
   ```

## :computer: API usage

1. **create API object and set zip code (EC4M 7RF - London postcode)**
   ```
   api_client = Client("EC4M 7RF")
   ```
   or
   ```
   api_client = Client()
   api_client.postcode = "EC4M 7RF"
   ```
2. **get restaurants**
   ```
   api_client.get_restaurants()   
   ```
   or
   ```
   api_client.restaurants
   ```