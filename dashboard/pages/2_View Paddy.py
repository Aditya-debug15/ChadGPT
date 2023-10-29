import ee
import folium
import geemap.colormaps as cm
import geemap.foliumap as geemap
from datetime import date
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

ee.Initialize()


# imports
def getTelanganaBoundary():
    Telangana = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level1").filter(
        ee.Filter.eq("ADM1_NAME", "Andhra Pradesh")
    )
    g = Telangana.geometry()
    return Telangana, g


def getMap():
    Map = geemap.Map(
        basemap="HYBRID",
        plugin_Draw=True,
        Draw_export=True,
        locate_control=True,
        plugin_LatLngPopup=False,
    )
    return Map


def getImageData(start_date, end_date, dist):
    data = (
        ee.ImageCollection("COPERNICUS/S1_GRD")
        .filterDate(start_date, end_date)
        .filter(ee.Filter.listContains("transmitterReceiverPolarisation", "VH"))
        .filter(ee.Filter.eq("instrumentMode", "IW"))
        .filter(
            ee.Filter.Or(
                ee.Filter.eq("orbitProperties_pass", "ASCENDING"),
                ee.Filter.eq("orbitProperties_pass", "DESCENDING"),
            )
        )
        .filterBounds(dist)
    )
    return data


rice1 = ee.FeatureCollection(
    [
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.76612554675451, 24.15676943925097],
                        [87.76569639331213, 24.155692611408448],
                        [87.76661907321325, 24.15483114259923],
                        [87.76721988803259, 24.155692611408448],
                        [87.76706968432775, 24.156417023865345],
                        [87.76666198855749, 24.156162501037766],
                    ]
                ]
            ),
            {"class": 1, "system:index": "0"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.8614615756291, 24.080855646393122],
                        [87.86189072907148, 24.080365889883],
                        [87.86219113648114, 24.081188679751307],
                    ]
                ]
            ),
            {"class": 1, "system:index": "1"},
        ),
    ]
)

rice2 = ee.FeatureCollection(
    [
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.83583271178601, 23.884259736067108],
                        [87.83624040755628, 23.883965433495757],
                        [87.8370557990968, 23.884671758542382],
                        [87.83596145781873, 23.884710998709693],
                    ]
                ]
            ),
            {"class": 2, "system:index": "0"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.84484493407605, 23.88773245585448],
                        [87.84473764571545, 23.887438161182395],
                        [87.84544574889539, 23.887085006692207],
                        [87.84544574889539, 23.88804636943346],
                    ]
                ]
            ),
            {"class": 2, "system:index": "1"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.56523229750982, 23.737520812388308],
                        [87.5667772499024, 23.73757973938117],
                        [87.56752826842657, 23.73964216734067],
                        [87.56615497741095, 23.73981894536089],
                    ]
                ]
            ),
            {"class": 2, "system:index": "2"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.56383754882208, 23.733807003292053],
                        [87.56506063613287, 23.733748074593038],
                        [87.56548978957525, 23.73496592895747],
                        [87.56503917846075, 23.73535878277609],
                        [87.56353714141241, 23.734298074747663],
                    ]
                ]
            ),
            {"class": 2, "system:index": "3"},
        ),
    ]
)

rice3 = ee.FeatureCollection(
    [
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.56577687013302, 23.697236559401848],
                        [87.56622748124752, 23.69721691099671],
                        [87.5662060235754, 23.6984645788546],
                        [87.56588415849362, 23.69867088498921],
                    ]
                ]
            ),
            {"class": 3, "system:index": "0"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.49052335914725, 23.63618049952557],
                        [87.49172498878592, 23.63647536292956],
                        [87.49157478508108, 23.63678988316182],
                        [87.4902444094097, 23.636671938163264],
                    ]
                ]
            ),
            {"class": 3, "system:index": "1"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.48170425590628, 23.643512572419937],
                        [87.48226215538138, 23.643296350946677],
                        [87.48271276649588, 23.64386638860559],
                        [87.48187591728323, 23.644023639936616],
                    ]
                ]
            ),
            {"class": 3, "system:index": "2"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.53802912243148, 23.915075780412543],
                        [87.5380505801036, 23.914918856529223],
                        [87.53845291145583, 23.914918856529223],
                        [87.5384475470378, 23.915090492016834],
                    ]
                ]
            ),
            {"class": 3, "system:index": "3"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.64468894555792, 23.89437541087259],
                        [87.64489279344305, 23.894326364325984],
                        [87.64492497995123, 23.894601024747377],
                        [87.6445601995252, 23.89464026190282],
                    ]
                ]
            ),
            {"class": 3, "system:index": "4"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.64955983712896, 23.892413534500662],
                        [87.64978514268621, 23.892452772319743],
                        [87.64978514268621, 23.892619532918033],
                        [87.64951692178472, 23.892599914035273],
                    ]
                ]
            ),
            {"class": 3, "system:index": "5"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.73093026292861, 23.832696917183544],
                        [87.73157399309218, 23.833128731581553],
                        [87.73131650102675, 23.83320724313584],
                        [87.7308015168959, 23.832893196633577],
                    ]
                ]
            ),
            {"class": 3, "system:index": "6"},
        ),
        ee.Feature(
            ee.Geometry.Polygon(
                [
                    [
                        [87.7231840432936, 23.833246498895157],
                        [87.72395651948989, 23.832932452487945],
                        [87.7240852655226, 23.833128731581553],
                        [87.72395651948989, 23.833482033201552],
                        [87.72333424699843, 23.833482033201552],
                    ]
                ]
            ),
            {"class": 3, "system:index": "7"},
        ),
    ]
)

rice4 = (
    ee.FeatureCollection(
        [
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.61273904593575, 23.681480175558644],
                            [87.61340423377145, 23.680979079847752],
                            [87.61370464118112, 23.6811952390176],
                            [87.61278196127999, 23.682177776190958],
                        ]
                    ]
                ),
                {"class": 4, "system:index": "0"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.60649486334908, 23.678198454999364],
                            [87.60689183028329, 23.677884034331232],
                            [87.60716005118478, 23.67837531629268],
                            [87.60676308425057, 23.678591479770507],
                        ]
                    ]
                ),
                {"class": 4, "system:index": "1"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.67514510582028, 23.93285429703097],
                            [87.67525239418087, 23.932560105093994],
                            [87.67544551322995, 23.9327268139406],
                            [87.67523093650875, 23.93328577732582],
                            [87.67473741005001, 23.93286410341733],
                        ]
                    ]
                ),
                {"class": 4, "system:index": "2"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.6715294880682, 23.93523722701145],
                            [87.67173333595333, 23.935345095229128],
                            [87.67170114944516, 23.935737342533525],
                            [87.67144365737973, 23.935600056112573],
                        ]
                    ]
                ),
                {"class": 4, "system:index": "3"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.66389055679379, 23.935286258030665],
                            [87.66376181076107, 23.934982265411353],
                            [87.6641265911871, 23.93496265295971],
                            [87.66420169303952, 23.935286258030665],
                        ]
                    ]
                ),
                {"class": 4, "system:index": "4"},
            ),
        ]
    ),
)
rice5 = (
    ee.FeatureCollection(
        [
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.87679190522407, 24.041477208769617],
                            [87.87703330403541, 24.041384126616236],
                            [87.87711377030585, 24.04144781441267],
                            [87.8770493972895, 24.04158498802081],
                        ]
                    ]
                ),
                {"class": 5, "system:index": "0"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.87988181000922, 24.043167372978846],
                            [87.87972624188636, 24.043030201060773],
                            [87.880021284878, 24.043049797058046],
                        ]
                    ]
                ),
                {"class": 5, "system:index": "1"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.87727189418048, 24.047620737694768],
                            [87.87740600463123, 24.04742968339457],
                            [87.87755620833606, 24.04742968339457],
                            [87.8774006402132, 24.047782398803673],
                        ]
                    ]
                ),
                {"class": 5, "system:index": "2"},
            ),
        ]
    ),
)
urban = (
    ee.FeatureCollection(
        [
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.6919148344055, 23.831691104952657],
                            [87.69457558574827, 23.828236511230827],
                            [87.69637803020628, 23.83180887357154],
                            [87.69328812542112, 23.83330060015566],
                        ]
                    ]
                ),
                {"class": 7, "system:index": "0"},
            )
        ]
    ),
)
water = (
    ee.FeatureCollection(
        [
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.70849088611753, 23.828717411891407],
                            [87.70853380146177, 23.82909035403357],
                            [87.70835141124876, 23.82919831076934],
                            [87.7081797498718, 23.828737040451948],
                        ]
                    ]
                ),
                {"class": 8, "system:index": "0"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.4121841791016, 23.83893944141689],
                            [87.41604656008305, 23.831166910528147],
                            [87.41990894106449, 23.833836317087535],
                            [87.41347163942875, 23.839803027204738],
                        ]
                    ]
                ),
                {"class": 8, "system:index": "1"},
            ),
        ]
    ),
)
other = (
    ee.FeatureCollection(
        [
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.44016498354496, 23.842629267750105],
                            [87.4393066766602, 23.838075849877555],
                            [87.44145244387211, 23.83768330636749],
                        ]
                    ]
                ),
                {"class": 9, "system:index": "0"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.40497440126957, 23.83784032391412],
                            [87.40617603090824, 23.83352227210844],
                            [87.40806430605473, 23.836348649545045],
                        ]
                    ]
                ),
                {"class": 9, "system:index": "1"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.45023526423229, 23.864295064702574],
                            [87.45418347590221, 23.864373557379785],
                            [87.45572842829479, 23.866571333027043],
                            [87.45006360285534, 23.866649824324632],
                        ]
                    ]
                ),
                {"class": 9, "system:index": "2"},
            ),
            ee.Feature(
                ee.Geometry.Polygon(
                    [
                        [
                            [87.63270912432917, 23.942353041607294],
                            [87.63172207141169, 23.94105868732994],
                            [87.63159332537897, 23.940117330610075],
                            [87.63356743121393, 23.94043111694634],
                            [87.63562736773737, 23.94196081440942],
                            [87.63489780688532, 23.942941380168673],
                            [87.63300953173884, 23.94243148690381],
                        ]
                    ]
                ),
                {"class": 9, "system:index": "3"},
            ),
        ]
    ),
)
geometry = ee.Geometry.Polygon(
    [
        [
            [87.14857421875001, 24.052360717693016],
            [87.14857421875001, 23.115988232721644],
            [88.19227539062501, 23.115988232721644],
            [88.19227539062501, 24.052360717693016],
        ]
    ]
)
admin2 = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level1")

Map = getMap()
dist = geometry
# Define Telangana administrative boundary
Telangana, geometry2 = getTelanganaBoundary()
dist2 = geometry2

Map.centerObject(geometry2, 6)

# Style parameters for Telangana
styleParams = {
    "fillColor": "b5ffb4",
    "color": "00909F",
    "width": 1.0,
}

# Add Telangana to the map
Map.addLayer(Telangana, styleParams, "Telangana")

# Define Sentinel-1 image collections for different date ranges
date_ranges = [
    ("2021-06-01", "2021-06-15"),
    ("2021-06-16", "2021-06-30"),
    ("2021-07-01", "2021-07-15"),
    ("2021-07-16", "2021-07-31"),
    ("2021-08-01", "2021-08-15"),
    ("2021-08-16", "2021-08-31"),
    ("2021-09-01", "2021-09-15"),
    ("2021-09-16", "2021-09-30"),
    ("2021-10-01", "2021-10-15"),
    ("2021-10-16", "2021-10-31"),
]

sentinel_collections = []
for i, date_range in enumerate(date_ranges):
    sentinel_collection = getImageData(date_range[0], date_range[1], dist)
    sentinel_collection = sentinel_collection.select("VH").mean().rename(f"VH{i + 1}")
    sentinel_collections.append(sentinel_collection)

# Merge the image collections
stacked = sentinel_collections[0].addBands(
    [sentinel_collection for sentinel_collection in sentinel_collections[1:]]
)

# Clip the stacked images to the region of interest
stacked = stacked.clip(dist)


sentinel_collections2 = []
for i, date_range in enumerate(date_ranges):
    sentinel_collection = getImageData(date_range[0], date_range[1], dist2)
    sentinel_collection = sentinel_collection.select("VH").mean().rename(f"VH{i + 1}")
    sentinel_collections2.append(sentinel_collection)

# Merge the image collections
stacked2 = sentinel_collections2[0].addBands(
    [sentinel_collection for sentinel_collection in sentinel_collections2[1:]]
)

# Clip the stacked images to the region of interest
stacked2 = stacked2.clip(dist2)

# Scale and convert to uint8
stacked_scaled = stacked.multiply(10).add(350).uint8()
stacked_scaled2 = stacked2.multiply(10).add(350).uint8()

bands = ["VH2", "VH4", "VH9"]
display = {"bands": bands, "min": 0, "max": 220}
# Map.addLayer(stacked_scaled, display, 'stacked')

# Define the Sentinel-2 image collection
S2_collection = (
    ee.ImageCollection("COPERNICUS/S2_SR")
    .filterDate("2021-09-25", "2021-11-05")
    .filterBounds(dist)
)

# Calculate the median image and clip it to the region of interest
im = S2_collection.median().clip(dist)

# Define bands and display parameters for Sentinel-2
S2_bands = ["B8", "B4", "B3"]
S2_display = {"bands": S2_bands, "min": 0, "max": 4000}

# Add Sentinel-2 image to the map
# Map.addLayer(im, S2_display, 'im')
# Map.setCenter(87.61, 23.84, 8)

gt1 = (
    rice1.merge(rice2)
    .merge(rice3)
    .merge(rice4)
    .merge(rice5)
    .merge(urban)
    .merge(water)
    .merge(other)
)

# Sample training data
training = stacked_scaled.sampleRegions(collection=gt1, properties=["class"], scale=10)

# Train a Random Forest classifier
classifier = ee.Classifier.smileRandomForest(10).train(
    features=training, classProperty="class"
)

# Classify the stacked image
classified = stacked_scaled.classify(classifier)

# Update the classified image mask
masked = classified.updateMask(classified.lt(6))

# Classify the validation data
validated = stacked_scaled2.classify(classifier)

# Update the validated image mask
masked2 = validated.updateMask(validated.lt(6))

Map.addLayer(
    masked2,
    {"min": 1, "max": 5, "palette": ["yellow", "blue", "orange", "cyan", "purple"]},
    "classification",
)
Map.addLayerControl()


st.markdown("### Distribution of different categories of paddy fields in Telangana")
# Display the map
st_map = Map.to_streamlit(height=600, bidirectional=True)


st.markdown("### Analysis of different categories of paddy fields")
# Load data file ee-chart.csv
data = pd.read_csv("./data/ee-chart.csv")
bandInfo = [
    "June_1FN",
    "June_2FN",
    "July_1FN",
    "July_2FN",
    "Aug_1FN",
    "Aug_2FN",
    "Sep_1FN",
    "Sep_2FN",
    "Oct_1FN",
    "Oct_2FN",
]

# Create a scatter plot
fig, ax = plt.subplots()
# read header names
cols = list(data.columns)
for c in cols[1:]:
    ax.plot(data["Property"], data[c], label=c)

# Set the plot title and axis labels
ax.set_title("Temporal Signatures - Backscatter")
ax.set_xlabel("Dates")
ax.set_ylabel("Backscatter(scaled)")
ax.set_xticks(data["Property"])
ax.set_xticklabels(bandInfo, rotation=45)
# set y range 0 to 250
ax.set_ylim([0, 250])

# Add a legend to the plot
ax.legend()

# Show the plot
st.pyplot(fig)


def getMapData(str):
    roi = Map.st_last_draw(st_map)
    geo = roi["geometry"]
    # calculate area of the selected region
    area = ee.Geometry(geo).area().divide(1000 * 1000).getInfo()
    # print the area of the selected region
    st.write("Area of the selected region is:", area, "square kilometers")

    masked_image = masked2.visualize(
        **{
            "min": 1,
            "max": 5,
            "palette": ["yellow", "blue", "orange", "cyan", "purple"],
        }
    )
    # Calculate the area of each class
    masked2_area = masked_image.reduceRegion(
        reducer=ee.Reducer.count().unweighted(), geometry=geo, scale=10
    ).getInfo()

    st.write(masked2_area)

    # print the area of the selected region
    # st.write("Area of the selected region under paddy cultivation is:", masked2_area['classification'], "square meters")


# Add sidebar to take user text input
st.sidebar.markdown("### Select the output name for the map")
str = st.sidebar.text_input("Output name", "map.tif")
if st.sidebar.button("Generate map"):
    getMapData(str)
    st.sidebar.success("Map generated successfully")
