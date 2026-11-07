import sys
import numpy as np

def calculate_car_price(year_val, mileage_val):
    year_val = float(year_val)
    mileage_val = float(mileage_val)

    
    
    year_score = np.clip((year_val - 2000) / 26.0, 0.0, 1.0)
    
    
    mileage_score = 1.0 - np.clip(mileage_val / 300000.0, 0.0, 1.0)
    
    fuzzy_weight = (year_score * 0.55) + (mileage_score * 0.45)
    
    min_price = 1000.0
    max_price = 50000.0
    
    calculated_price = min_price + (max_price - min_price) * (fuzzy_weight ** 1.2)
    
    return float(calculated_price)

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("ERROR: Missing arguments")
        sys.exit(1)
        
    try:
        in_year = float(sys.argv[1])
        in_mileage = float(sys.argv[2])
        estimated_price = calculate_car_price(in_year, in_mileage)
        print(f"{estimated_price:.2f}")
    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)
