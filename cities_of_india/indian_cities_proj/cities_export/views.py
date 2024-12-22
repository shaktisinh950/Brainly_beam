import requests
import csv
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

def export_indian_cities_to_csv(request):
    # API endpoint
    url = "https://countriesnow.space/api/v0.1/countries/cities"
    
    # Payload (filter for India)
    payload = {
        "country": "India"
    }

    try:
        # Send POST request to fetch cities
        response = requests.post(url, json=payload)

        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            if not data.get("error"):
                # Fetch city list
                cities = data.get("data", [])

                # Create the HttpResponse object with CSV header
                response = HttpResponse(content_type='text/csv')
                response['Content-Disposition'] = 'attachment; filename="indian_cities.csv"'

                # Create a CSV writer
                writer = csv.writer(response)
                writer.writerow(['City Name'])  # Header row

                # Write city names to the CSV
                for city in cities:
                    writer.writerow([city])

                return response
            else:
                return JsonResponse({
                    "status": "error",
                    "message": data.get("msg", "Unknown error")
                }, status=400)
        else:
            return JsonResponse({
                "status": "error",
                "message": "Failed to fetch data",
                "status_code": response.status_code
            }, status=response.status_code)
    except Exception as e:
        return JsonResponse({
            "status": "error",
            "message": str(e)
        }, status=500)

# Add this new view
def download_page(request):
    return render(request, 'cities_export/download.html')