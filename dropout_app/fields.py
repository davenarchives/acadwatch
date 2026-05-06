YES_NO_OPTIONS = [
    ("1", "Yes"),
    ("0", "No"),
]

GENDER_OPTIONS = [
    ("1", "Male"),
    ("0", "Female"),
]

APPLICATION_ORDER_OPTIONS = [
    (str(value), f"{value} - {'First choice' if value == 0 else 'Choice rank'}")
    for value in range(10)
]

APPLICATION_MODE_OPTIONS = [
    ("1", "1 - 1st phase - general contingent"),
    ("2", "2 - Ordinance No. 612/93"),
    ("5", "5 - 1st phase - special contingent (Azores Island)"),
    ("7", "7 - Holders of other higher courses"),
    ("10", "10 - Ordinance No. 854-B/99"),
    ("15", "15 - International student (bachelor)"),
    ("16", "16 - 1st phase - special contingent (Madeira Island)"),
    ("17", "17 - 2nd phase - general contingent"),
    ("18", "18 - 3rd phase - general contingent"),
    ("26", "26 - Ordinance No. 533-A/99, item b2 (Different Plan)"),
    ("27", "27 - Ordinance No. 533-A/99, item b3 (Other Institution)"),
    ("39", "39 - Over 23 years old"),
    ("42", "42 - Transfer"),
    ("43", "43 - Change of course"),
    ("44", "44 - Technological specialization diploma holders"),
    ("51", "51 - Change of institution/course"),
    ("53", "53 - Short cycle diploma holders"),
    ("57", "57 - Change of institution/course (International)"),
]

COURSE_OPTIONS = [
    ("33", "33 - Biofuel Production Technologies"),
    ("171", "171 - Animation and Multimedia Design"),
    ("8014", "8014 - Social Service (evening attendance)"),
    ("9003", "9003 - Agronomy"),
    ("9070", "9070 - Communication Design"),
    ("9085", "9085 - Veterinary Nursing"),
    ("9119", "9119 - Informatics Engineering"),
    ("9130", "9130 - Equinculture"),
    ("9147", "9147 - Management"),
    ("9238", "9238 - Social Service"),
    ("9254", "9254 - Tourism"),
    ("9500", "9500 - Nursing"),
    ("9556", "9556 - Oral Hygiene"),
    ("9670", "9670 - Advertising and Marketing Management"),
    ("9773", "9773 - Journalism and Communication"),
    ("9853", "9853 - Basic Education"),
    ("9991", "9991 - Management (evening attendance)"),
]

PREVIOUS_QUALIFICATION_OPTIONS = [
    ("1", "1 - Secondary education"),
    ("2", "2 - Higher education - bachelor's degree"),
    ("3", "3 - Higher education - degree"),
    ("4", "4 - Higher education - master's"),
    ("5", "5 - Higher education - doctorate"),
    ("6", "6 - Frequency of higher education"),
    ("9", "9 - 12th year of schooling - not completed"),
    ("10", "10 - 11th year of schooling - not completed"),
    ("12", "12 - Other - 11th year of schooling"),
    ("14", "14 - 10th year of schooling"),
    ("15", "15 - 10th year of schooling - not completed"),
    ("19", "19 - Basic education 3rd cycle or equivalent"),
    ("38", "38 - Basic education 2nd cycle or equivalent"),
    ("39", "39 - Technological specialization course"),
    ("40", "40 - Higher education - degree (1st cycle)"),
    ("42", "42 - Professional higher technical course"),
    ("43", "43 - Higher education - master (2nd cycle)"),
]

MOTHER_QUALIFICATION_OPTIONS = [
    ("1", "1 - Secondary Education - 12th Year or equivalent"),
    ("2", "2 - Higher Education - Bachelor's Degree"),
    ("3", "3 - Higher Education - Degree"),
    ("4", "4 - Higher Education - Master's"),
    ("5", "5 - Higher Education - Doctorate"),
    ("6", "6 - Frequency of Higher Education"),
    ("9", "9 - 12th Year of Schooling - Not Completed"),
    ("10", "10 - 11th Year of Schooling - Not Completed"),
    ("11", "11 - 7th Year (Old)"),
    ("12", "12 - Other - 11th Year of Schooling"),
    ("14", "14 - 10th Year of Schooling"),
    ("18", "18 - General commerce course"),
    ("19", "19 - Basic Education 3rd Cycle or equivalent"),
    ("22", "22 - Technical-professional course"),
    ("26", "26 - 7th year of schooling"),
    ("27", "27 - 2nd cycle of the general high school course"),
    ("29", "29 - 9th Year of Schooling - Not Completed"),
    ("30", "30 - 8th year of schooling"),
    ("34", "34 - Unknown"),
    ("35", "35 - Can't read or write"),
    ("36", "36 - Can read without having a 4th year of schooling"),
    ("37", "37 - Basic education 1st cycle or equivalent"),
    ("38", "38 - Basic Education 2nd Cycle or equivalent"),
    ("39", "39 - Technological specialization course"),
    ("40", "40 - Higher education - degree (1st cycle)"),
    ("41", "41 - Specialized higher studies course"),
    ("42", "42 - Professional higher technical course"),
    ("43", "43 - Higher Education - Master (2nd cycle)"),
    ("44", "44 - Higher Education - Doctorate (3rd cycle)"),
]

FATHER_QUALIFICATION_OPTIONS = MOTHER_QUALIFICATION_OPTIONS + [
    ("13", "13 - 2nd year complementary high school course"),
    ("20", "20 - Complementary High School Course"),
    ("25", "25 - Complementary High School Course - not concluded"),
    ("31", "31 - General Course of Administration and Commerce"),
    ("33", "33 - Supplementary Accounting and Administration"),
]

MOTHER_OCCUPATION_OPTIONS = [
    ("0", "0 - Student"),
    ("1", "1 - Legislative/executive representatives, directors, managers"),
    ("2", "2 - Specialists in intellectual and scientific activities"),
    ("3", "3 - Intermediate level technicians and professions"),
    ("4", "4 - Administrative staff"),
    ("5", "5 - Personal services, security workers and sellers"),
    ("6", "6 - Farmers and skilled agriculture, fisheries and forestry workers"),
    ("7", "7 - Skilled industry, construction and craft workers"),
    ("8", "8 - Installation and machine operators and assembly workers"),
    ("9", "9 - Unskilled workers"),
    ("10", "10 - Armed Forces professions"),
    ("90", "90 - Other situation"),
    ("99", "99 - Blank"),
    ("122", "122 - Health professionals"),
    ("123", "123 - Teachers"),
    ("125", "125 - ICT specialists"),
    ("131", "131 - Science and engineering technicians"),
    ("132", "132 - Health technicians and professionals"),
    ("134", "134 - Legal, social, sports and cultural technicians"),
    ("141", "141 - Office workers and data processing operators"),
    ("143", "143 - Data, accounting, statistical and financial operators"),
    ("144", "144 - Other administrative support staff"),
    ("151", "151 - Personal service workers"),
    ("152", "152 - Sellers"),
    ("153", "153 - Personal care workers"),
    ("171", "171 - Skilled construction workers"),
    ("173", "173 - Printing, precision, jewelers and artisan workers"),
    ("175", "175 - Food, woodworking, clothing and craft workers"),
    ("191", "191 - Cleaning workers"),
    ("192", "192 - Unskilled agriculture, fisheries and forestry workers"),
    ("193", "193 - Unskilled construction, manufacturing and transport workers"),
    ("194", "194 - Meal preparation assistants"),
]

FATHER_OCCUPATION_OPTIONS = MOTHER_OCCUPATION_OPTIONS + [
    ("101", "101 - Armed Forces Officers"),
    ("102", "102 - Armed Forces Sergeants"),
    ("103", "103 - Other Armed Forces personnel"),
    ("112", "112 - Directors of administrative and commercial services"),
    ("114", "114 - Hotel, catering, trade and service directors"),
    ("121", "121 - Physical sciences, mathematics and engineering specialists"),
    ("124", "124 - Finance, accounting and public relations specialists"),
    ("135", "135 - Information and communication technology technicians"),
    ("154", "154 - Protection and security services personnel"),
    ("161", "161 - Market-oriented agricultural and animal production workers"),
    ("163", "163 - Subsistence farmers, fishers, hunters and gatherers"),
    ("172", "172 - Metallurgy and metalworking skilled workers"),
    ("174", "174 - Electricity and electronics skilled workers"),
    ("181", "181 - Fixed plant and machine operators"),
    ("182", "182 - Assembly workers"),
    ("183", "183 - Vehicle drivers and mobile equipment operators"),
    ("195", "195 - Street vendors and street service providers"),
]

FEATURE_FIELDS = [
    {
        "name": "Curricular units 2nd sem (approved)",
        "label": "2nd Semester Units Approved",
        "help": "Number of curricular units approved in the second semester.",
    },
    {
        "name": "Curricular units 2nd sem (grade)",
        "label": "2nd Semester Grade Average",
        "help": "Average second semester grade, typically between 0 and 20.",
    },
    {
        "name": "Curricular units 1st sem (approved)",
        "label": "1st Semester Units Approved",
        "help": "Number of curricular units approved in the first semester.",
    },
    {
        "name": "Tuition fees up to date",
        "label": "Tuition Fees Up To Date",
        "help": "Use 1 for yes and 0 for no.",
    },
    {
        "name": "Curricular units 1st sem (grade)",
        "label": "1st Semester Grade Average",
        "help": "Average first semester grade, typically between 0 and 20.",
    },
    {
        "name": "Age at enrollment",
        "label": "Age At Enrollment",
        "help": "Student age at the time of enrollment.",
    },
    {
        "name": "Admission grade",
        "label": "Admission Grade",
        "help": "Admission grade, typically between 0 and 200.",
    },
    {
        "name": "Curricular units 2nd sem (evaluations)",
        "label": "2nd Semester Evaluations",
        "help": "Number of evaluations in second semester curricular units.",
    },
    {
        "name": "Previous qualification (grade)",
        "label": "Previous Qualification Grade",
        "help": "Previous qualification grade, typically between 0 and 200.",
    },
    {
        "name": "Course",
        "label": "Course",
        "help": "Course code used by the trained model.",
    },
    {
        "name": "Curricular units 1st sem (evaluations)",
        "label": "1st Semester Evaluations",
        "help": "Number of evaluations in first semester curricular units.",
    },
    {
        "name": "Father's occupation",
        "label": "Father's Occupation",
        "help": "Occupation category code.",
    },
    {
        "name": "Mother's occupation",
        "label": "Mother's Occupation",
        "help": "Occupation category code.",
    },
    {
        "name": "GDP",
        "label": "GDP",
        "help": "GDP value for the relevant period.",
    },
    {
        "name": "Application mode",
        "label": "Application Mode",
        "help": "Application mode code.",
    },
    {
        "name": "Mother's qualification",
        "label": "Mother's Qualification",
        "help": "Qualification category code.",
    },
    {
        "name": "Father's qualification",
        "label": "Father's Qualification",
        "help": "Qualification category code.",
    },
    {
        "name": "Scholarship holder",
        "label": "Scholarship Holder",
        "help": "Use 1 for yes and 0 for no.",
    },
    {
        "name": "Debtor",
        "label": "Debtor",
        "help": "Use 1 for yes and 0 for no.",
    },
    {
        "name": "Curricular units 2nd sem (enrolled)",
        "label": "2nd Semester Units Enrolled",
        "help": "Number of curricular units enrolled in the second semester.",
    },
    {
        "name": "Curricular units 1st sem (enrolled)",
        "label": "1st Semester Units Enrolled",
        "help": "Number of curricular units enrolled in the first semester.",
    },
    {
        "name": "Previous qualification",
        "label": "Previous Qualification",
        "help": "Previous qualification category code.",
    },
    {
        "name": "Displaced",
        "label": "Displaced",
        "help": "Use 1 for yes and 0 for no.",
    },
    {
        "name": "Curricular units 2nd sem (without evaluations)",
        "label": "2nd Semester Units Without Evaluations",
        "help": "Number of second semester units without evaluations.",
    },
    {
        "name": "Curricular units 1st sem (without evaluations)",
        "label": "1st Semester Units Without Evaluations",
        "help": "Number of first semester units without evaluations.",
    },
    {
        "name": "Inflation rate",
        "label": "Inflation Rate",
        "help": "Inflation rate percentage.",
    },
    {
        "name": "Unemployment rate",
        "label": "Unemployment Rate",
        "help": "Unemployment rate percentage.",
    },
    {
        "name": "Gender",
        "label": "Gender",
        "help": "Use 1 for male and 0 for female.",
    },
    {
        "name": "Application order",
        "label": "Application Order",
        "help": "Application order from 0 for first choice to 9 for last choice.",
    },
]

FIELD_OPTIONS = {
    "Application mode": APPLICATION_MODE_OPTIONS,
    "Application order": APPLICATION_ORDER_OPTIONS,
    "Course": COURSE_OPTIONS,
    "Previous qualification": PREVIOUS_QUALIFICATION_OPTIONS,
    "Mother's qualification": MOTHER_QUALIFICATION_OPTIONS,
    "Father's qualification": FATHER_QUALIFICATION_OPTIONS,
    "Mother's occupation": MOTHER_OCCUPATION_OPTIONS,
    "Father's occupation": FATHER_OCCUPATION_OPTIONS,
    "Displaced": YES_NO_OPTIONS,
    "Debtor": YES_NO_OPTIONS,
    "Tuition fees up to date": YES_NO_OPTIONS,
    "Gender": GENDER_OPTIONS,
    "Scholarship holder": YES_NO_OPTIONS,
}

SECTION_META = {
    "Academic Performance": {
        "icon": "graduation-cap",
        "description": "Grades, unit progress, and semester performance signals.",
    },
    "Personal Information": {
        "icon": "user-round",
        "description": "Basic student context used by the trained model.",
    },
    "Socioeconomic Factors": {
        "icon": "landmark",
        "description": "Financial, household, and macroeconomic context.",
    },
    "Enrollment Details": {
        "icon": "clipboard-list",
        "description": "Application, course, and prior qualification details.",
    },
}

FIELD_SECTIONS = {
    "Curricular units 2nd sem (approved)": "Academic Performance",
    "Curricular units 2nd sem (grade)": "Academic Performance",
    "Curricular units 1st sem (approved)": "Academic Performance",
    "Curricular units 1st sem (grade)": "Academic Performance",
    "Admission grade": "Academic Performance",
    "Curricular units 2nd sem (evaluations)": "Academic Performance",
    "Previous qualification (grade)": "Academic Performance",
    "Curricular units 1st sem (evaluations)": "Academic Performance",
    "Curricular units 2nd sem (enrolled)": "Academic Performance",
    "Curricular units 1st sem (enrolled)": "Academic Performance",
    "Curricular units 2nd sem (without evaluations)": "Academic Performance",
    "Curricular units 1st sem (without evaluations)": "Academic Performance",
    "Age at enrollment": "Personal Information",
    "Gender": "Personal Information",
    "Displaced": "Personal Information",
    "Father's occupation": "Socioeconomic Factors",
    "Mother's occupation": "Socioeconomic Factors",
    "GDP": "Socioeconomic Factors",
    "Mother's qualification": "Socioeconomic Factors",
    "Father's qualification": "Socioeconomic Factors",
    "Scholarship holder": "Socioeconomic Factors",
    "Debtor": "Socioeconomic Factors",
    "Tuition fees up to date": "Socioeconomic Factors",
    "Inflation rate": "Socioeconomic Factors",
    "Unemployment rate": "Socioeconomic Factors",
    "Course": "Enrollment Details",
    "Application mode": "Enrollment Details",
    "Previous qualification": "Enrollment Details",
    "Application order": "Enrollment Details",
}

FIELD_UI = {
    "Curricular units 2nd sem (approved)": {"type": "number", "min": 0, "max": 30, "step": 1, "default": 6, "unit": "units", "placeholder": "6"},
    "Curricular units 2nd sem (grade)": {"type": "number", "min": 0, "max": 20, "step": 0.1, "default": 12, "unit": "/20", "placeholder": "12.0"},
    "Curricular units 1st sem (approved)": {"type": "number", "min": 0, "max": 30, "step": 1, "default": 6, "unit": "units", "placeholder": "6"},
    "Curricular units 1st sem (grade)": {"type": "number", "min": 0, "max": 20, "step": 0.1, "default": 12, "unit": "/20", "placeholder": "12.0"},
    "Admission grade": {"type": "number", "min": 0, "max": 200, "step": 0.1, "default": 130, "unit": "/200", "placeholder": "130.0"},
    "Curricular units 2nd sem (evaluations)": {"type": "number", "min": 0, "max": 40, "step": 1, "default": 8, "unit": "evals", "placeholder": "8"},
    "Previous qualification (grade)": {"type": "number", "min": 0, "max": 200, "step": 0.1, "default": 130, "unit": "/200", "placeholder": "130.0"},
    "Curricular units 1st sem (evaluations)": {"type": "number", "min": 0, "max": 40, "step": 1, "default": 8, "unit": "evals", "placeholder": "8"},
    "Curricular units 2nd sem (enrolled)": {"type": "number", "min": 0, "max": 30, "step": 1, "default": 6, "unit": "units", "placeholder": "6"},
    "Curricular units 1st sem (enrolled)": {"type": "number", "min": 0, "max": 30, "step": 1, "default": 6, "unit": "units", "placeholder": "6"},
    "Curricular units 2nd sem (without evaluations)": {"type": "number", "min": 0, "max": 20, "step": 1, "default": 0, "unit": "units", "placeholder": "0"},
    "Curricular units 1st sem (without evaluations)": {"type": "number", "min": 0, "max": 20, "step": 1, "default": 0, "unit": "units", "placeholder": "0"},
    "Age at enrollment": {"type": "number", "min": 16, "max": 70, "step": 1, "default": 20, "unit": "years", "placeholder": "20"},
    "GDP": {"type": "number", "default": 0, "unit": "index", "placeholder": "0.0"},
    "Inflation rate": {"type": "number", "default": 0, "unit": "%", "placeholder": "0.0"},
    "Unemployment rate": {"type": "number", "default": 10, "unit": "%", "placeholder": "10.0"},
}

TOGGLE_FIELDS = {
    "Displaced",
    "Debtor",
    "Tuition fees up to date",
    "Gender",
    "Scholarship holder",
}

for field in FEATURE_FIELDS:
    field["options"] = FIELD_OPTIONS.get(field["name"])
    field["section"] = FIELD_SECTIONS.get(field["name"], "Enrollment Details")
    field.update(FIELD_UI.get(field["name"], {"type": "select" if field["options"] else "number"}))
    if field["name"] in TOGGLE_FIELDS:
        field["type"] = "toggle"
    if "default" not in field:
        field["default"] = field["options"][0][0] if field["options"] else 0

def default_form_values():
    """Return defaults so the dashboard can show an initial live estimate."""
    return {field["name"]: str(field["default"]) for field in FEATURE_FIELDS}


def grouped_fields():
    """Group fields for the dashboard accordion layout."""
    sections = []
    for title, meta in SECTION_META.items():
        fields = [field for field in FEATURE_FIELDS if field["section"] == title]
        sections.append({"title": title, **meta, "fields": fields})
    return sections
