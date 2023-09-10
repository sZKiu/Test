from ..models.data import Sector, Subsector, db

def insert_sectors_and_subsectors():
    sectors_data = [
    {
        "id": "1",
        "name": "Manufacturing",
        "subsectors": [
            {"id": "19", "name": "Construction materials"},
            {"id": "18", "name": "Electronics and Optics"},
            {
                "id": "6",
                "name": "Food and Beverage",
                "subsubsectors": [
                    {"id": "342", "name": "Bakery & confectionery products"},
                    {"id": "43", "name": "Beverages"},
                    {"id": "42", "name": "Fish & fish products"},
                    {"id": "40", "name": "Meat & meat products"},
                    {"id": "39", "name": "Milk & dairy products"},
                    {"id": "437", "name": "Other"},
                    {"id": "378", "name": "Sweets & snack food"}
                ]
            },
            {
                "id": "13",
                "name": "Furniture",
                "subsubsectors": [
                    {"id": "389", "name": "Bathroom/sauna"},
                    {"id": "385", "name": "Bedroom"},
                    {"id": "390", "name": "Children’s room"},
                    {"id": "98", "name": "Kitchen"},
                    {"id": "101", "name": "Living room"},
                    {"id": "392", "name": "Office"},
                    {"id": "394", "name": "Other (Furniture)"},
                    {"id": "341", "name": "Outdoor"},
                    {"id": "99", "name": "Project furniture"}
                ]
            },
            {
                "id": "12",
                "name": "Machinery",
                "subsubsectors": [
                    {"id": "94", "name": "Machinery components"},
                    {"id": "91", "name": "Machinery equipment/tools"},
                    {"id": "224", "name": "Manufacture of machinery"},
                    {
                        "id": "97",
                        "name": "Maritime",
                        "subsubsectors": [
                            {"id": "271", "name": "Aluminium and steel workboats"},
                            {"id": "269", "name": "Boat/Yacht building"},
                            {"id": "230", "name": "Ship repair and conversion"}
                        ]
                    },
                    {"id": "93", "name": "Metal structures"},
                    {"id": "508", "name": "Other"},
                    {"id": "227", "name": "Repair and maintenance service"}
                ]
            },
            {
                "id": "11",
                "name": "Metalworking",
                "subsubsectors": [
                    {"id": "67", "name": "Construction of metal structures"},
                    {"id": "263", "name": "Houses and buildings"},
                    {"id": "267", "name": "Metal products"},
                    {
                        "id": "542",
                        "name": "Metal works",
                        "subsubsectors": [
                            {"id": "75", "name": "CNC-machining"},
                            {"id": "62", "name": "Forgings, Fasteners"},
                            {"id": "69", "name": "Gas, Plasma, Laser cutting"},
                            {"id": "66", "name": "MIG, TIG, Aluminum welding"}
                        ]
                    }
                ]
            },
            {
                "id": "9",
                "name": "Plastic and Rubber",
                "subsubsectors": [
                    {"id": "54", "name": "Packaging"},
                    {"id": "556", "name": "Plastic goods"},
                    {
                        "id": "559",
                        "name": "Plastic processing technology",
                        "subsubsectors": [
                            {"id": "55", "name": "Blowing"},
                            {"id": "57", "name": "Moulding"},
                            {"id": "53", "name": "Plastics welding and processing"}
                        ]
                    },
                    {"id": "560", "name": "Plastic profiles"}
                ]
            },
            {
                "id": "5",
                "name": "Printing",
                "subsubsectors": [
                    {"id": "148", "name": "Advertising"},
                    {"id": "150", "name": "Book/Periodicals printing"},
                    {"id": "145", "name": "Labelling and packaging printing"}
                ]
            },
            {
                "id": "7",
                "name": "Textile and Clothing",
                "subsubsectors": [
                    {"id": "44", "name": "Clothing"},
                    {"id": "45", "name": "Textile"}
                ]
            },
            {
                "id": "8",
                "name": "Wood",
                "subsubsectors": [
                    {"id": "337", "name": "Other (Wood)"},
                    {"id": "51", "name": "Wooden building materials"},
                    {"id": "47", "name": "Wooden houses"}
                ]
            }
        ]
    },
    {
        "id": "3",
        "name": "Other",
        "subsectors": [
            {"id": "37", "name": "Creative industries"},
            {"id": "29", "name": "Energy technology"},
            {"id": "33", "name": "Environment"},
            # ...otros subsectores
        ]
    },
    {
        "id": "2",
        "name": "Service",
        "subsectors": [
            {"id": "25", "name": "Business services"},
            {"id": "35", "name": "Engineering"},
            {
                "id": "28",
                "name": "Information Technology and Telecommunications",
                "subsubsectors": [
                    {"id": "581", "name": "Data processing, Web portals, E-marketing"},
                    {"id": "576", "name": "Programming, Consultancy"},
                    {"id": "121", "name": "Software, Hardware"},
                    {"id": "122", "name": "Telecommunications"},
                ]
            },
            {"id": "22", "name": "Tourism"},
            {"id": "141", "name": "Translation services"},
            {
                "id": "21",
                "name": "Transport and Logistics",
                "subsubsectors": [
                    {"id": "111", "name": "Air"},
                    {"id": "114", "name": "Rain"},
                    {"id": "112", "name": "Road"},
                    {"id": "113", "name": "Water"}
                ]
            }
        ]
    }
]

    for sector_data in sectors_data:
        sector = Sector(id=sector_data['id'], name=sector_data['name'])
        db.session.add(sector)

        for subsector_data in sector_data['subsectors']:
            subsector = Subsector(id=subsector_data['id'], name=subsector_data['name'], sector_id=sector.id)
            db.session.add(subsector)

        db.session.commit()

def clear_tables():
    Subsector.query.delete()
    Sector.query.delete()
    db.session.commit()