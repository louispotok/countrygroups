"""
unfccc_groups
-------------

"""

from ._version import get_versions
__version__ = get_versions()['version']
del get_versions


ANNEX_ONE = [
    "AUS",
    "AUT",
    "BLR",
    "BEL",
    "BGR",
    "CAN",
    "HRV",
    "CYP",
    "CZE",
    "DNK",
    "EST",
    "EUU",
    "FIN",
    "FRA",
    "DEU",
    "GRC",
    "HUN",
    "ISL",
    "IRL",
    "ITA",
    "JPN",
    "LVA",
    "LIE",
    "LTU",
    "LUX",
    "MLT",
    "MCO",
    "NLD",
    "NZL",
    "NOR",
    "POL",
    "PRT",
    "ROU",
    "RUS",
    "SVK",
    "SVN",
    "ESP",
    "SWE",
    "CHE",
    "TUR",
    "UKR",
    "GBR",
    "USA"
]

EU_MEMBERS = [
    "AUT",
    "BEL",
    "BGR",
    "HRV",
    "CYP",
    "CZE",
    "DNK",
    "EST",
    "FIN",
    "FRA",
    "DEU",
    "GRC",
    "HUN",
    "IRL",
    "ITA",
    "LVA",
    "LTU",
    "LUX",
    "MLT",
    "NLD",
    "POL",
    "PRT",
    "ROU",
    "SVK",
    "SVN",
    "ESP",
    "SWE",
    "GBR"
]

G20 = [
    "AUS",
    "ARG",
    "BRA",
    "CAN",
    "CHN",
    "EUU",
    "FRA",
    "DEU",
    "IND",
    "IDN",
    "ITA",
    "JPN",
    "MEX",
    "RUS",
    "SAU",
    "ZAF",
    "KOR",
    "TUR",
    "GBR",
    "USA"
]

G7 = [
    "CAN",
    "FRA",
    "DEU",
    "ITA",
    "JPN",
    "GBR",
    "USA",
    "EUU"
]

GRADUATED_LDCS = [
    "BWA",
    "MDV",
    "CPV",
    "WSM",
    "GNQ"
]

LDCS = [
    "AFG",
    "AGO",
    "BGD",
    "BEN",
    "BTN",
    "BFA",
    "BDI",
    "KHM",
    "CAF",
    "TCD",
    "COM",
    "COD",
    "DJI",
    "ERI",
    "ETH",
    "GMB",
    "GIN",
    "GNB",
    "HTI",
    "KIR",
    "LAO",
    "LSO",
    "LBR",
    "MDG",
    "MWI",
    "MLI",
    "MRT",
    "MOZ",
    "MMR",
    "NPL",
    "NER",
    "RWA",
    "STP",
    "SEN",
    "SLE",
    "SLB",
    "SOM",
    "SSD",
    "SDN",
    "TZA",
    "TLS",
    "TGO",
    "TUV",
    "UGA",
    "VUT",
    "YEM",
    "ZMB"
]

NON_ANNEX_ONE = [
    "AFG",
    "ALB",
    "DZA",
    "AND",
    "AGO",
    "ATG",
    "ARG",
    "ARM",
    "AZE",
    "BHS",
    "BHR",
    "BGD",
    "BRB",
    "BLZ",
    "BEN",
    "BTN",
    "BOL",
    "BIH",
    "BWA",
    "BRA",
    "BRN",
    "BFA",
    "BDI",
    "KHM",
    "CPV",
    "CMR",
    "CAF",
    "TCD",
    "CHL",
    "CHN",
    "COL",
    "COM",
    "COG",
    "COK",
    "CRI",
    "CUB",
    "CIV",
    "PRK",
    "COD",
    "DJI",
    "DMA",
    "DOM",
    "ECU",
    "EGY",
    "SLV",
    "GNQ",
    "ERI",
    "ETH",
    "FJI",
    "GAB",
    "GMB",
    "GEO",
    "GHA",
    "GRD",
    "GTM",
    "GIN",
    "GNB",
    "GUY",
    "HTI",
    "HND",
    "IND",
    "IDN",
    "IRN",
    "IRQ",
    "ISR",
    "JAM",
    "JOR",
    "KAZ",
    "KEN",
    "KIR",
    "KWT",
    "KGZ",
    "LAO",
    "LBN",
    "LSO",
    "LBR",
    "LBY",
    "MDG",
    "MWI",
    "MYS",
    "MDV",
    "MLI",
    "MHL",
    "MRT",
    "MUS",
    "MEX",
    "FSM",
    "MNG",
    "MNE",
    "MAR",
    "MOZ",
    "MMR",
    "NAM",
    "NRU",
    "NPL",
    "NIC",
    "NER",
    "NGA",
    "NIU",
    "OMN",
    "PAK",
    "PLW",
    "PSE",
    "PAN",
    "PNG",
    "PRY",
    "PER",
    "PHL",
    "QAT",
    "KOR",
    "MDA",
    "RWA",
    "KNA",
    "LCA",
    "VCT",
    "WSM",
    "SMR",
    "STP",
    "SAU",
    "SEN",
    "SRB",
    "SYC",
    "SLE",
    "SGP",
    "SLB",
    "SOM",
    "ZAF",
    "SSD",
    "LKA",
    "SDN",
    "SUR",
    "SWZ",
    "SYR",
    "TJK",
    "THA",
    "MKD",
    "TLS",
    "TGO",
    "TON",
    "TTO",
    "TUN",
    "TKM",
    "TUV",
    "UGA",
    "ARE",
    "TZA",
    "URY",
    "UZB",
    "VUT",
    "VEN",
    "VNM",
    "YEM",
    "ZMB",
    "ZWE"
]

SIDS = [
    "CPV",
    "COM",
    "GNB",
    "MDV",
    "MUS",
    "STP",
    "SYC",
    "SGP",
    "ATG",
    "BHS",
    "BRB",
    "BLZ",
    "CUB",
    "DMA",
    "DOM",
    "GRD",
    "GUY",
    "HTI",
    "JAM",
    "KNA",
    "LCA",
    "VCT",
    "SUR",
    "TTO",
    "FJI",
    "KIR",
    "MHL",
    "FSM",
    "NRU",
    "PLW",
    "PNG",
    "WSM",
    "SLB",
    "TLS",
    "TON",
    "TUV",
    "VUT"
]

UNFCCC = [
    "AFG",
    "ALB",
    "DZA",
    "AND",
    "AGO",
    "ATG",
    "ARG",
    "ARM",
    "AUS",
    "AUT",
    "AZE",
    "BHS",
    "BHR",
    "BGD",
    "BRB",
    "BLR",
    "BEL",
    "BLZ",
    "BEN",
    "BTN",
    "BOL",
    "BIH",
    "BWA",
    "BRA",
    "BRN",
    "BGR",
    "BFA",
    "BDI",
    "CPV",
    "KHM",
    "CMR",
    "CAN",
    "CAF",
    "TCD",
    "CHL",
    "CHN",
    "COL",
    "COM",
    "COG",
    "COK",
    "CRI",
    "CIV",
    "HRV",
    "CUB",
    "CYP",
    "CZE",
    "PRK",
    "COD",
    "DNK",
    "DJI",
    "DMA",
    "DOM",
    "ECU",
    "EGY",
    "SLV",
    "GNQ",
    "ERI",
    "EST",
    "ETH",
    "EUU",
    "FJI",
    "FIN",
    "FRA",
    "GAB",
    "GMB",
    "GEO",
    "DEU",
    "GHA",
    "GRC",
    "GRD",
    "GTM",
    "GIN",
    "GNB",
    "GUY",
    "HTI",
    "HND",
    "HUN",
    "ISL",
    "IND",
    "IDN",
    "IRN",
    "IRQ",
    "IRL",
    "ISR",
    "ITA",
    "JAM",
    "JPN",
    "JOR",
    "KAZ",
    "KEN",
    "KIR",
    "KWT",
    "KGZ",
    "LAO",
    "LVA",
    "LBN",
    "LSO",
    "LBR",
    "LBY",
    "LIE",
    "LTU",
    "LUX",
    "MDG",
    "MWI",
    "MYS",
    "MDV",
    "MLI",
    "MLT",
    "MHL",
    "MRT",
    "MUS",
    "MEX",
    "FSM",
    "MCO",
    "MNG",
    "MNE",
    "MAR",
    "MOZ",
    "MMR",
    "NAM",
    "NRU",
    "NPL",
    "NLD",
    "NZL",
    "NIC",
    "NER",
    "NGA",
    "NIU",
    "NOR",
    "OMN",
    "PAK",
    "PLW",
    "PAN",
    "PNG",
    "PRY",
    "PER",
    "PHL",
    "POL",
    "PRT",
    "QAT",
    "KOR",
    "MDA",
    "ROU",
    "RUS",
    "RWA",
    "KNA",
    "LCA",
    "VCT",
    "WSM",
    "SMR",
    "STP",
    "SAU",
    "SEN",
    "SRB",
    "SYC",
    "SLE",
    "SGP",
    "SVK",
    "SVN",
    "PSE",
    "SLB",
    "SOM",
    "ZAF",
    "SSD",
    "ESP",
    "LKA",
    "SDN",
    "SUR",
    "SWZ",
    "SWE",
    "CHE",
    "SYR",
    "TJK",
    "THA",
    "MKD",
    "TLS",
    "TGO",
    "TON",
    "TTO",
    "TUN",
    "TUR",
    "TKM",
    "TUV",
    "UGA",
    "UKR",
    "ARE",
    "GBR",
    "TZA",
    "USA",
    "URY",
    "UZB",
    "VUT",
    "VEN",
    "VNM",
    "YEM",
    "ZMB",
    "ZWE"
]

