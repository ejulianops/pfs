import random
from datetime import datetime, timedelta

import names
import pandas as pd

# Lists of UK town names
uk_towns = [
    "London",
    "Birmingham",
    "Manchester",
    "Leeds",
    "Sheffield",
    "Bristol",
    "Liverpool",
    "Nottingham",
    "Leicester",
    "Newcastle",
    "Southampton",
    "Portsmouth",
    "Brighton",
    "Norwich",
    "Cardiff",
    "Swansea",
    "Newport",
    "Edinburgh",
    "Glasgow",
    "Aberdeen",
    "Dundee",
    "Belfast",
    "Derry",
    "Oxford",
    "Cambridge",
    "Canterbury",
    "York",
    "Bath",
    "Exeter",
    "Lincoln",
    "Chester",
    "Durham",
    "St Albans",
    "Salisbury",
    "Wells",
    "Winchester",
    "Chichester",
    "Hereford",
    "Worcester",
    "Gloucester",
    "Carlisle",
    "Plymouth",
    "Bradford",
    "Hull",
    "Stoke",
    "Wolverhampton",
    "Derby",
    "Salford",
    "Bournemouth",
    "Middlesbrough",
    "Blackpool",
    "Bolton",
    "Preston",
    "Bury",
    "Rochdale",
    "Oldham",
    "Stockport",
    "Halifax",
    "Huddersfield",
    "Wakefield",
    "Barnsley",
    "Doncaster",
    "Rotherham",
    "Dudley",
    "Walsall",
    "West Bromwich",
    "Wigan",
    "Southport",
    "Crewe",
    "Macclesfield",
    "Chesterfield",
    "Mansfield",
    "Loughborough",
    "Nuneaton",
    "Coventry",
    "Solihull",
    "Sutton Coldfield",
    "Epsom",
    "Guildford",
    "Reading",
    "Slough",
    "Milton Keynes",
    "Luton",
    "Basildon",
    "Chelmsford",
    "Colchester",
    "Ipswich",
    "Bedford",
    "Watford",
    "Hemel Hempstead",
    "St Albans",
    "Peterborough",
    "Northampton",
]

# Business name generators
business_prefix = [
    "Apex",
    "Castle",
    "City",
    "Coastal",
    "Central",
    "Crown",
    "Diamond",
    "East",
    "Empire",
    "Fairway",
    "First",
    "Global",
    "Golden",
    "Grand",
    "Green",
    "Highland",
    "Kings",
    "Lakes",
    "Majestic",
    "Metro",
    "Midland",
    "Northern",
    "Oak",
    "Park",
    "Premier",
    "Prime",
    "Queens",
    "Regal",
    "Royal",
    "Seaside",
    "Silver",
    "Southern",
    "Sterling",
    "Summit",
    "Sunset",
    "Thames",
    "Tower",
    "Union",
    "Valley",
    "West",
    "Wharf",
    "Woodland",
    "York",
    "Abbey",
    "Arlington",
    "Ashford",
    "Aston",
    "Barton",
]

business_suffix = [
    "Group",
    "Traders",
    "Supplies",
    "Retail",
    "Foods",
    "Stores",
    "Distributors",
    "Enterprises",
    "Solutions",
    "Holdings",
    "Partners",
    "Associates",
    "Merchants",
    "Wholesale",
    "Logistics",
    "Marketing",
    "Media",
    "Technologies",
    "Innovations",
]

# First names for emails
first_names = [
    "john",
    "james",
    "robert",
    "michael",
    "william",
    "david",
    "richard",
    "joseph",
    "thomas",
    "charles",
    "christopher",
    "daniel",
    "matthew",
    "anthony",
    "donald",
    "mark",
    "paul",
    "steven",
    "andrew",
    "kenneth",
    "joshua",
    "kevin",
    "brian",
    "george",
    "timothy",
    "ronald",
    "edward",
    "jason",
    "jeffrey",
    "ryan",
    "jacob",
    "gary",
    "nicholas",
    "eric",
    "jonathan",
    "stephen",
    "larry",
    "justin",
    "scott",
    "brandon",
    "benjamin",
    "samuel",
    "raymond",
    "gregory",
    "frank",
    "alexander",
    "patrick",
    "jack",
    "dennis",
    "jerry",
    "tyler",
    "aaron",
    "jose",
    "nathan",
    "adam",
    "henry",
    "zachary",
    "taylor",
    "sarah",
    "emma",
    "laura",
    "emily",
    "jessica",
    "ashley",
    "amanda",
    "olivia",
    "sophia",
    "isabella",
    "charlotte",
    "mia",
    "amelia",
    "harper",
    "evelyn",
    "abigail",
    "ella",
    "elizabeth",
    "camila",
    "luna",
    "sofia",
    "ava",
    "madison",
    "layla",
    "chloe",
    "penelope",
    "riley",
    "zoey",
    "nora",
    "lily",
    "eleanor",
    "hannah",
    "aria",
    "scarlett",
]


# Generate clients with multiple sites
def generate_clients_with_sites(num_rows=100):
    # First, create a pool of clients (25-30 distinct clients)
    num_clients = random.randint(25, 30)
    clients = []

    for i in range(num_clients):
        client_name = (
            f"{random.choice(business_prefix)} {random.choice(business_suffix)}"
        )
        # Each client will have 2-5 sites
        num_sites = random.randint(2, 5)

        # Select random towns for this client (unique)
        available_towns = uk_towns.copy()
        random.shuffle(available_towns)
        site_towns = available_towns[:num_sites]

        # Generate site codes for this client
        site_codes = []
        used_codes = set()
        for _ in range(num_sites):
            while True:
                code = f"9{random.randint(100, 999):03d}"
                if code not in used_codes:
                    used_codes.add(code)
                    site_codes.append(code)
                    break

        clients.append(
            {
                "client_name": client_name,
                "site_towns": site_towns,
                "site_codes": site_codes,
            }
        )

    # Now generate rows up to num_rows
    data = []
    row_count = 0
    used_codes_global = set()

    while row_count < num_rows:
        # Pick a random client
        client = random.choice(clients)

        # Select a site for this client
        site_index = random.randint(0, len(client["site_towns"]) - 1)
        site_code = client["site_codes"][site_index]
        site_name = client["site_towns"][site_index]

        # Store email - always site code
        store_email = f"{site_code}@psgroup.com"

        # Generate emails with some randomness
        def random_person_email():
            return (
                f"{random.choice(first_names)}.{random.choice(first_names)}@psgroup.com"
            )

        # Buying email - 40% store, 60% random person
        buying_email = store_email if random.random() < 0.4 else random_person_email()

        # Special buying - 40% store, 60% random person
        special_buying_email = (
            store_email if random.random() < 0.4 else random_person_email()
        )

        # CRE - always random person
        cre_email = random_person_email()

        # CRM - 40% store, 60% random person
        crm_email = store_email if random.random() < 0.4 else random_person_email()

        # Last updated - random date/time in June 2026
        days_offset = random.randint(0, 30)
        hours = random.randint(0, 23)
        minutes = random.randint(0, 59)
        seconds = random.randint(0, 59)
        last_updated = datetime(2026, 6, 1, 0, 0, 0) + timedelta(
            days=days_offset, hours=hours, minutes=minutes, seconds=seconds
        )
        last_updated_str = last_updated.strftime("%Y-%m-%d %H:%M:%S")

        data.append(
            {
                "client": client["client_name"],
                "site code": site_code,
                "site name": site_name,
                "store": store_email,
                "buying": buying_email,
                "special buying": special_buying_email,
                "cre": cre_email,
                "crm": crm_email,
                "last updated": last_updated_str,
            }
        )

        row_count += 1

    return data


# Generate the data
data = generate_clients_with_sites(100)

# Create DataFrame
df = pd.DataFrame(data)

# Save to CSV
df.to_csv("data.csv", index=False)

# Display preview
print("First 20 rows of the dataset:")
print(df.head(20).to_string())

# Show client distribution
print(f"\n{'=' * 60}")
print(f"Total rows: {len(df)}")
print(f"Unique clients: {df['client'].nunique()}")
print(f"Unique site codes: {df['site code'].nunique()}")
print(f"Unique towns: {df['site name'].nunique()}")

# Show how many sites each client has
client_site_counts = df.groupby("client").size().sort_values(ascending=False)
print(f"\nClient site distribution:")
print(client_site_counts.head(10))

# Show example of a client with multiple sites
print(f"\n{'=' * 60}")
print("Example: First client with all their sites:")
first_client = df["client"].iloc[0]
print(
    df[df["client"] == first_client][["client", "site code", "site name"]].to_string(
        index=False
    )
)
