cities = {
    'taipei': {
        'country': 'taiwan',
        'population': 2_511_000,
        'fact': 'night market',
        },
    'bali': {
        'country': 'indonesia',
        'population': 4_317_000,
        'fact': 'kecak',
        },
    'billund': {
        'country': 'denpark',
        'population': 6_725,
        'fact': 'legoland',
        }
    }

for city, city_info in cities.items():
    country = city_info['country'].title()
    population = city_info['population']
    fact = city_info['fact'].title()

    print(f"\n{city.title()}は{country}にあります。")
    print(f"  人口は約{population}人です。")
    print(f"  特徴として{fact}があります。")
