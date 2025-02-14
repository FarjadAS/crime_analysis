import dash
from dash import html

dash.register_page(__name__, path='/', name="About")

####################### PAGE LAYOUT #############################
layout = html.Div(children=[
    html.Div(children=[
        html.H2("Los Angeles Crime Dataset Analysis"),
        "This report provides an in-depth analysis of Los Angeles crime data to reveal meaningful insights about the city and crime trends and patterns.Using multi-year data, the study uses advanced statistical methods to examine various dimensions of crime, including but not limited to spatial distribution, temporal variation, and prevalence of crime types..",
        html.Br(),html.Br(),
        "The results of this analysis help to understand the more complex dynamics of crime in Los Angeles and provide insights that can inform policy decisions, resource allocation, and the development of targeted interventions. As cities around the world grapple with the challenge of public safety, this report serves as a model for leveraging data analytics to provide insights into crime prevention and urban safety.",
        html.Br(), html.Br(),
        "To better understand the report following are Data Variables",
    ]),
    html.Div(children=[
        html.Br(),
        html.H2("Data Variables"),
        html.B("DR_NO: "), "Division of Records Number: Official file number made up of a 2-digit year, area ID, and 5 digits",
        html.Br(),
        html.B("Date Rptd: "), " MM/DD/YYYY",
        html.Br(),
        html.B("DATE OCC: "), "MM/DD/YYYY",
        html.Br(),
        html.B("TIME OCC: "), "In 24-hour military time",
        html.Br(),
        html.B("AREA: "), "The LAPD has 21 Community Police Stations referred to as Geographic Areas within the department. These Geogrphic Areas are sequentially numbered from 1-21.",
        html.Br(),
        html.B("AREA NAME: "), "The 21 Geographic Areas or Patrol Divisions are also given a name designation that references a landmark or the surrounding community that it is responsible for. For example, the 77th Street Division is located at the intersection of South Broadway and 77th Street, serving neighborhoods in South Los Angeles",
        html.Br(),
        html.B("Rpt Dist No: "), "A four-digit code that represents a sub-area within a Geographic Area. All crime records reference the 'RD' that it occurred in for statistical comparisons. Find LAPD Reporting Districts on the LA City GeoHub at http://geohub.lacity.org/datasets/c4f83909b81d4786aa8ba8a74a4b4db1_4",
        html.Br(),
        html.B("Crm Cd: "), "Indicates the crime committed. (Same as Crime Code 1)",
        html.Br(),
        html.B(" Crm Cd Desc: "), "Defines the Crime Code provided",
        html.Br(),
        html.B("Vict Age: "), "Two-character numeric",
        html.Br(),
        html.B("Vict Sex: "), ": F - Female M - Male X - Unknown",
        html.Br(),
        html.B("Vict Descent: "), "Descent Code: A - Other Asian B - Black C - Chinese D - Cambodian F - Filipino G - Guamanian H -Hispanic/Latin/Mexican I - American Indian/Alaskan Native J - Japanese K - Korean L - Laotian O - Other P - Pacific Islander S - Samoan U - Hawaiian V - Vietnamese W - White X - Unknown Z - Asian Indian",
        html.Br(),
        html.B("Status: "), "Status of the case. (IC is the default)",
        html.Br(),
        html.B("Status Desc: "), "Defines the Status Code provided",
        html.Br(),
        html.B("LOCATION: "), " Street address of crime incident rounded to the nearest hundred blocks to maintain anonymity",
        html.Br(),
        html.B("LAT: "), "Latitude",
        html.Br(),
        html.B("LON: "), "Longitude",
        html.Br(),
        html.B("Hour: "), "Hour from Time OCC",
        html.Br(),
        html.B("Month: "), "Month from DATE OCC",
        html.Br(),
        html.H2("BE SAFE"),
        html.Img(src="/assets/los.jpg", alt="Los Angeles Crime"),
        html.Br(),
        html.P("Los Angeles"),
        html.Br(),
        html.H2("Crime Cloud"),
        html.Img(src="/assets/word.jpeg", alt="Los Angeles Crime"),
        html.Br(),
        html.P("Word Cloud"),
    ]),
], className="bg-light p-4 m-2")