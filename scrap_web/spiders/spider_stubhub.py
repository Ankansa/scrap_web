import scrapy
import json


class Stubhub(scrapy.Spider):
    name = "events"
    start_urls = ["https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODkwMw%3D%3D&lon=LTgwLjQ3OTIxOTY%3D&to=253402300799999&tlcId=2"]

    def parse(self, responce):

        responce_object = responce.json()
        events = responce_object.get("events", None)
        event_list = []

        for info in events:
            title = info.get("name", None)
            date = info.get("formattedDateWithoutYear", None)
            time = info.get("formattedTime", None)
            venue = info.get("venueName", None)
            formattedVenueLocation = info.get("formattedVenueLocation", None)
            linkToImage = info.get("imageUrl", None)
            data = {
                "title": title,
                "datetime": f"{date} {time}",
                "location": f"{venue} {formattedVenueLocation}",
                "linkToImage": linkToImage
            }
            event_list.append(data)
            
        for i in range(0, len(event_list), 5):
            chunk = event_list[i:i+5]
            if len(chunk) >= 5:
                file_name = f'op_json_{i//5 + 1}.json'
                with open(file_name, 'w') as json_file:
                    json.dump({"events": chunk}, json_file)
                
                yield {
                    "events": chunk
                }