# data.py — India Government Schemes, Jobs, Exams, Yojanas Database

SCHEMES = [
    {
        "id": "pm_kisan",
        "name": "PM Kisan Samman Nidhi",
        "hindi_name": "पीएम किसान सम्मान निधि",
        "category": "Agriculture",
        "description": "Rs 6000/year direct income support to small and marginal farmers in 3 installments of Rs 2000.",
        "eligibility": "Small/marginal farmers with less than 2 hectares land. Must be Indian citizen.",
        "documents": ["Aadhaar Card", "Land records (Khatoni)", "Bank Passbook", "Mobile Number"],
        "how_to_apply": "1. Go to pmkisan.gov.in\n2. Click 'Farmers Corner'\n3. Click 'New Farmer Registration'\n4. Enter Aadhaar number\n5. Fill in land and bank details\n6. Submit and wait for verification",
        "website": "https://pmkisan.gov.in",
        "benefit": "₹6,000/year",
        "tags": ["farmer", "kisan", "agriculture", "money", "kheti"]
    },
    {
        "id": "ayushman",
        "name": "Ayushman Bharat - PM Jan Arogya Yojana",
        "hindi_name": "आयुष्मान भारत - पीएम जन आरोग्य योजना",
        "category": "Health",
        "description": "Health insurance of Rs 5 lakh per year per family for secondary and tertiary hospitalization.",
        "eligibility": "Poor and vulnerable families as per SECC 2011 database. No age/family size limit.",
        "documents": ["Aadhaar Card", "Ration Card", "SECC list verification"],
        "how_to_apply": "1. Visit pmjay.gov.in or nearest empanelled hospital\n2. Check eligibility using mobile number or ration card\n3. If eligible, get Ayushman card made at hospital or CSC center\n4. Use card at any empanelled government/private hospital",
        "website": "https://pmjay.gov.in",
        "benefit": "₹5 Lakh health cover/year",
        "tags": ["health", "hospital", "insurance", "ayushman", "medical", "swasthya"]
    },
    {
        "id": "ujjwala",
        "name": "Pradhan Mantri Ujjwala Yojana",
        "hindi_name": "प्रधानमंत्री उज्ज्वला योजना",
        "category": "Women / Energy",
        "description": "Free LPG connection to women from BPL households to replace traditional cooking fuels.",
        "eligibility": "Women above 18 years from BPL households. SC/ST, PMAY beneficiaries given priority.",
        "documents": ["Aadhaar Card", "BPL ration card", "Bank account details", "Passport size photo"],
        "how_to_apply": "1. Visit nearest LPG distributor (HP/Bharat/Indane)\n2. Fill KYC form\n3. Submit documents\n4. Get free connection with first cylinder",
        "website": "https://pmuy.gov.in",
        "benefit": "Free LPG connection + subsidy",
        "tags": ["lpg", "gas", "women", "ujjwala", "cooking", "mahila", "bpl"]
    },
    {
        "id": "pm_awas",
        "name": "Pradhan Mantri Awas Yojana (Urban)",
        "hindi_name": "प्रधानमंत्री आवास योजना (शहरी)",
        "category": "Housing",
        "description": "Affordable housing for urban poor. Interest subsidy of up to Rs 2.67 lakh on home loans.",
        "eligibility": "EWS (income up to ₹3L), LIG (₹3L-6L), MIG-I (₹6L-12L), MIG-II (₹12L-18L). No pucca house anywhere in India.",
        "documents": ["Aadhaar Card", "Income certificate", "Address proof", "Bank statements", "Property documents"],
        "how_to_apply": "1. Visit pmaymis.gov.in\n2. Click 'Citizen Assessment'\n3. Select category (Slum/CLSS etc.)\n4. Enter Aadhaar number\n5. Fill application form\n6. Submit and note application number",
        "website": "https://pmaymis.gov.in",
        "benefit": "Up to ₹2.67 lakh subsidy",
        "tags": ["house", "ghar", "awas", "home", "housing", "loan", "subsidy"]
    },
    {
        "id": "mudra",
        "name": "PM Mudra Yojana",
        "hindi_name": "पीएम मुद्रा योजना",
        "category": "Business / Loan",
        "description": "Loans up to Rs 10 lakh for small businesses and entrepreneurs without collateral.",
        "eligibility": "Any Indian citizen with a business plan for non-farm income generating activities.",
        "documents": ["Aadhaar Card", "PAN Card", "Business plan", "Address proof", "Bank statements (6 months)"],
        "how_to_apply": "1. Visit mudra.org.in\n2. Choose loan type: Shishu (up to 50K), Kishor (50K-5L), Tarun (5L-10L)\n3. Visit nearest bank/NBFC/MFI\n4. Submit application with documents\n5. Bank processes within 7-10 days",
        "website": "https://www.mudra.org.in",
        "benefit": "Loan ₹50K to ₹10 Lakh (no collateral)",
        "tags": ["loan", "business", "mudra", "entrepreneur", "startup", "vyapar", "shop"]
    },
    {
        "id": "sukanya",
        "name": "Sukanya Samriddhi Yojana",
        "hindi_name": "सुकन्या समृद्धि योजना",
        "category": "Girl Child / Savings",
        "description": "Savings scheme for girl child with high interest rate (8.2%) and tax benefits.",
        "eligibility": "Girl child below 10 years of age. One account per girl, max 2 girls per family.",
        "documents": ["Girl's birth certificate", "Parent/guardian Aadhaar", "Parent/guardian PAN", "Address proof"],
        "how_to_apply": "1. Visit any post office or authorized bank\n2. Fill SSY account opening form\n3. Submit documents and minimum ₹250\n4. Account matures after 21 years",
        "website": "https://www.indiapost.gov.in",
        "benefit": "8.2% interest + tax benefit under 80C",
        "tags": ["girl", "beti", "sukanya", "savings", "daughter", "education", "bachchi"]
    },
    {
        "id": "atal_pension",
        "name": "Atal Pension Yojana",
        "hindi_name": "अटल पेंशन योजना",
        "category": "Pension",
        "description": "Guaranteed pension of Rs 1000-5000/month after age 60 for unorganized sector workers.",
        "eligibility": "Indian citizens aged 18-40 years with a savings bank account. Not an income tax payer.",
        "documents": ["Aadhaar Card", "Savings bank account", "Mobile number"],
        "how_to_apply": "1. Visit your bank or post office\n2. Fill APY registration form\n3. Link with savings account for auto-debit\n4. Choose pension amount (1K/2K/3K/4K/5K)\n5. Auto-debit starts monthly",
        "website": "https://npscra.nsdl.co.in",
        "benefit": "₹1,000–₹5,000/month pension after 60",
        "tags": ["pension", "retirement", "atal", "old age", "budhapa", "monthly"]
    },
    {
        "id": "jan_dhan",
        "name": "Pradhan Mantri Jan Dhan Yojana",
        "hindi_name": "प्रधानमंत्री जन धन योजना",
        "category": "Banking",
        "description": "Zero balance bank account with RuPay debit card, accident insurance of Rs 2 lakh.",
        "eligibility": "Any Indian citizen above 10 years without a bank account.",
        "documents": ["Aadhaar Card OR Voter ID OR Driving License", "Passport size photo"],
        "how_to_apply": "1. Visit any nationalized bank\n2. Ask for Jan Dhan account opening form\n3. Submit Aadhaar + photo\n4. Account opened same day\n5. Get RuPay card in 7-10 days",
        "website": "https://pmjdy.gov.in",
        "benefit": "Zero balance account + ₹2L accident insurance",
        "tags": ["bank", "account", "jan dhan", "banking", "rupay", "card"]
    },
]

YOJANAS = [
    {
        "id": "beti_bachao",
        "name": "Beti Bachao Beti Padhao",
        "hindi_name": "बेटी बचाओ बेटी पढ़ाओ",
        "category": "Women / Education",
        "description": "Scheme to address declining Child Sex Ratio and promote welfare of girl child education.",
        "eligibility": "Girl children across India, especially in districts with low sex ratio.",
        "documents": ["Girl's birth certificate", "School enrollment proof"],
        "how_to_apply": "1. Enroll girl child in school\n2. Contact local Anganwadi center\n3. Register at wcd.nic.in\n4. District-level programs and scholarships available",
        "website": "https://wcd.nic.in",
        "benefit": "Education support, scholarships, awareness programs",
        "tags": ["beti", "girl", "education", "padhao", "bachao", "school"]
    },
    {
        "id": "swachh_bharat",
        "name": "Swachh Bharat Mission",
        "hindi_name": "स्वच्छ भारत मिशन",
        "category": "Sanitation",
        "description": "Free toilet construction for BPL households. Rs 12,000 incentive for building toilet.",
        "eligibility": "BPL households, SC/ST families, small/marginal farmers without toilet.",
        "documents": ["Aadhaar Card", "BPL certificate", "Bank account"],
        "how_to_apply": "1. Visit swachhbharatmission.gov.in\n2. Or visit gram panchayat office\n3. Fill application for toilet construction\n4. Get ₹12,000 in bank after construction verified",
        "website": "https://swachhbharatmission.gov.in",
        "benefit": "₹12,000 for toilet construction",
        "tags": ["toilet", "swachh", "sanitation", "bathroom", "shauchalay", "bpl"]
    },
    {
        "id": "digital_india",
        "name": "Digital India",
        "hindi_name": "डिजिटल इंडिया",
        "category": "Technology",
        "description": "Free digital literacy training, internet access, and online government services.",
        "eligibility": "All Indian citizens. Special focus on rural areas.",
        "documents": ["Aadhaar Card"],
        "how_to_apply": "1. Visit digitalindia.gov.in\n2. Register for PMGDISHA (digital literacy)\n3. Find nearest CSC center\n4. Get free 20-hour digital literacy training",
        "website": "https://digitalindia.gov.in",
        "benefit": "Free digital training + internet access",
        "tags": ["digital", "internet", "computer", "literacy", "technology"]
    },
]

JOBS = [
    {
        "id": "ssc_cgl",
        "name": "SSC CGL (Combined Graduate Level)",
        "hindi_name": "एसएससी सीजीएल",
        "category": "Central Government",
        "description": "Recruitment for Group B and C posts in various central government ministries and departments.",
        "eligibility": "Graduate from recognized university. Age: 18-32 years (relaxation for SC/ST/OBC).",
        "documents": ["10th/12th marksheet", "Graduation certificate", "Aadhaar Card", "Caste certificate (if applicable)"],
        "how_to_apply": "1. Visit ssc.nic.in\n2. Register with email and mobile\n3. Fill online application form\n4. Upload photo and signature\n5. Pay fee (₹100, free for SC/ST/Women)\n6. Download admit card before exam",
        "website": "https://ssc.nic.in",
        "benefit": "Pay scale ₹25,500 – ₹81,100/month",
        "tags": ["ssc", "cgl", "graduate", "central government", "job", "naukri", "group b"]
    },
    {
        "id": "railway_ntpc",
        "name": "RRB NTPC (Railway Non-Technical Popular Categories)",
        "hindi_name": "आरआरबी एनटीपीसी",
        "category": "Railway",
        "description": "Recruitment for junior clerk, accounts clerk, commercial apprentice and other posts in Indian Railways.",
        "eligibility": "12th pass or Graduate (depending on post). Age: 18-33 years.",
        "documents": ["10th/12th marksheet", "Graduation certificate (if required)", "Aadhaar Card", "Caste certificate"],
        "how_to_apply": "1. Visit indianrailways.gov.in or rrbcdg.gov.in\n2. Register and create account\n3. Fill application form\n4. Upload photo/signature\n5. Pay fee online\n6. Appear for CBT (Computer Based Test)",
        "website": "https://www.rrbcdg.gov.in",
        "benefit": "Pay scale ₹19,900 – ₹35,400/month",
        "tags": ["railway", "rrb", "ntpc", "train", "12th pass", "job", "naukri", "rail"]
    },
    {
        "id": "bank_po",
        "name": "IBPS PO (Probationary Officer)",
        "hindi_name": "आईबीपीएस पीओ",
        "category": "Banking",
        "description": "Recruitment of Probationary Officers in public sector banks like PNB, BOB, Canara Bank etc.",
        "eligibility": "Graduate in any discipline. Age: 20-30 years.",
        "documents": ["Graduation certificate", "Aadhaar Card", "PAN Card", "Caste certificate (if applicable)"],
        "how_to_apply": "1. Visit ibps.in\n2. Register with valid email\n3. Fill CRP PO application\n4. Pay fees (₹175 for SC/ST, ₹850 for others)\n5. Appear for Prelims → Mains → Interview",
        "website": "https://www.ibps.in",
        "benefit": "Pay scale ₹36,000 – ₹63,840/month + perks",
        "tags": ["bank", "po", "ibps", "probationary", "banking", "job", "naukri"]
    },
    {
        "id": "upsc_ias",
        "name": "UPSC Civil Services (IAS/IPS/IFS)",
        "hindi_name": "यूपीएससी सिविल सेवा",
        "category": "Central Government",
        "description": "India's most prestigious exam for IAS, IPS, IFS and other Group A Central Services.",
        "eligibility": "Graduate from recognized university. Age: 21-32 (General), 21-35 (OBC), 21-37 (SC/ST). Attempts: 6 (General), 9 (OBC), unlimited (SC/ST).",
        "documents": ["Graduation certificate", "Aadhaar Card", "Caste certificate", "PWD certificate (if applicable)"],
        "how_to_apply": "1. Visit upsc.gov.in\n2. Register for One Time Registration (OTR)\n3. Fill Detailed Application Form (DAF)\n4. Pay fees ₹100 (free for SC/ST/Women/PWD)\n5. Prelims → Mains → Personality Test",
        "website": "https://upsc.gov.in",
        "benefit": "Pay scale ₹56,100 – ₹2,50,000/month (Cabinet Secretary)",
        "tags": ["upsc", "ias", "ips", "ifs", "civil services", "collector", "officer", "prestigious"]
    },
    {
        "id": "army_agniveer",
        "name": "Agnipath Scheme - Agniveer",
        "hindi_name": "अग्निपथ योजना - अग्निवीर",
        "category": "Defence",
        "description": "Short-term military service (4 years) in Indian Army, Navy or Air Force for youth.",
        "eligibility": "Age 17.5 to 23 years. 10th pass for most posts, 12th for technical posts. Physically fit.",
        "documents": ["10th/12th marksheet", "Aadhaar Card", "Birth certificate", "Domicile certificate"],
        "how_to_apply": "1. Visit joinindianarmy.nic.in / joinindiannavy.gov.in / airmenselection.cdac.in\n2. Register online\n3. Fill application form\n4. Appear for written test + physical test + medical\n5. Merit list published on website",
        "website": "https://joinindianarmy.nic.in",
        "benefit": "₹30,000–₹40,000/month + ₹11.71 lakh after 4 years",
        "tags": ["army", "military", "agniveer", "agnipath", "defence", "navy", "airforce", "sena"]
    },
    {
        "id": "nrega",
        "name": "MGNREGA (Mahatma Gandhi NREGA)",
        "hindi_name": "महात्मा गांधी नरेगा",
        "category": "Rural Employment",
        "description": "Guaranteed 100 days of wage employment per year to rural households.",
        "eligibility": "Any adult member of rural household willing to do unskilled manual work.",
        "documents": ["Aadhaar Card", "Ration Card", "Bank account"],
        "how_to_apply": "1. Visit gram panchayat office\n2. Register household for job card\n3. Get Job Card within 15 days\n4. Demand work at gram panchayat\n5. Work allocated within 15 days",
        "website": "https://nrega.nic.in",
        "benefit": "100 days guaranteed work at state minimum wage",
        "tags": ["nrega", "mgnrega", "100 days", "rural", "employment", "gaon", "village", "kaam"]
    },
]

EXAMS = [
    {
        "id": "jee",
        "name": "JEE Main & Advanced (IIT Entrance)",
        "hindi_name": "जेईई मेन और एडवांस्ड",
        "category": "Engineering Entrance",
        "description": "National level entrance exam for admission to IITs, NITs, IIITs and other engineering colleges.",
        "eligibility": "12th pass with PCM (Physics, Chemistry, Math). Min 75% marks (65% for SC/ST). Age limit: attempt in year of 12th or next year.",
        "documents": ["12th marksheet", "Class 10 certificate", "Aadhaar Card", "Category certificate if applicable"],
        "how_to_apply": "1. Visit jeemain.nta.nic.in\n2. Register with email and mobile\n3. Fill application form (session-wise)\n4. Upload photo, signature, documents\n5. Pay fees: ₹650-1300 (varies by category)\n6. Download admit card before exam",
        "website": "https://jeemain.nta.nic.in",
        "benefit": "Admission to IITs, NITs, IIITs (top engineering colleges)",
        "tags": ["jee", "iit", "engineering", "nit", "entrance", "12th", "maths", "pcm"]
    },
    {
        "id": "neet",
        "name": "NEET UG (Medical Entrance)",
        "hindi_name": "नीट यूजी",
        "category": "Medical Entrance",
        "description": "Single national entrance test for MBBS, BDS and AYUSH courses across India.",
        "eligibility": "12th pass with PCB (Physics, Chemistry, Biology). Min 50% marks. Age: 17 years minimum.",
        "documents": ["12th marksheet", "Class 10 certificate", "Aadhaar Card", "Passport size photo"],
        "how_to_apply": "1. Visit neet.nta.nic.in\n2. Register and create login\n3. Fill online application\n4. Upload photo and signature\n5. Pay fees: ₹1700 (General), ₹1000 (SC/ST/OBC)\n6. Appear for exam (pen & paper mode)",
        "website": "https://neet.nta.nic.in",
        "benefit": "Admission to MBBS/BDS/AYUSH in government & private colleges",
        "tags": ["neet", "mbbs", "medical", "doctor", "bds", "biology", "pcb", "12th"]
    },
    {
        "id": "cuet",
        "name": "CUET UG (Central University Entrance)",
        "hindi_name": "सीयूईटी यूजी",
        "category": "University Entrance",
        "description": "Common entrance test for admission to all central universities including DU, JNU, BHU etc.",
        "eligibility": "12th pass or appearing students. No minimum percentage required.",
        "documents": ["12th marksheet/admit card", "Aadhaar Card", "Category certificate if applicable"],
        "how_to_apply": "1. Visit cuet.samarth.ac.in\n2. Register with email/mobile\n3. Fill application, choose universities and subjects\n4. Pay fees: ₹550-800 depending on number of subjects\n5. Download admit card and appear for exam",
        "website": "https://cuet.samarth.ac.in",
        "benefit": "Admission to DU, JNU, BHU, AMU and 250+ universities",
        "tags": ["cuet", "du", "jnu", "bhu", "central university", "graduation", "12th", "college"]
    },
    {
        "id": "clat",
        "name": "CLAT (Law Entrance)",
        "hindi_name": "क्लैट",
        "category": "Law Entrance",
        "description": "Common Law Admission Test for admission to 22 National Law Universities (NLUs) in India.",
        "eligibility": "UG: 12th pass with 45% (40% for SC/ST). PG: LLB with 55%.",
        "documents": ["12th marksheet", "Aadhaar Card", "Category certificate if applicable"],
        "how_to_apply": "1. Visit consortiumofnlus.ac.in\n2. Register and fill application\n3. Pay fees: ₹4000 (General), ₹3500 (SC/ST)\n4. Appear for 2-hour offline exam\n5. Counselling based on merit",
        "website": "https://consortiumofnlus.ac.in",
        "benefit": "Admission to NLU Delhi, NLU Mumbai, NALSAR and other top law schools",
        "tags": ["clat", "law", "nlu", "lawyer", "llb", "legal", "advocate"]
    },
    {
        "id": "ctet",
        "name": "CTET (Teacher Eligibility Test)",
        "hindi_name": "सीटेट",
        "category": "Teaching",
        "description": "Central Teacher Eligibility Test for teaching in central government schools (KVS, NVS, etc.).",
        "eligibility": "Paper 1 (Class 1-5): D.El.Ed or B.El.Ed. Paper 2 (Class 6-8): Graduation + B.Ed.",
        "documents": ["Degree/Diploma certificate", "Aadhaar Card", "Photo and signature"],
        "how_to_apply": "1. Visit ctet.nic.in\n2. Register and fill application\n3. Choose Paper 1, Paper 2 or both\n4. Pay fees: ₹1000 (one paper), ₹1200 (both)\n5. Appear for exam\n6. Certificate valid for lifetime (from 2021)",
        "website": "https://ctet.nic.in",
        "benefit": "Eligibility to teach in KV, NV and central government schools",
        "tags": ["ctet", "teacher", "teaching", "school", "tet", "kvs", "nvs", "shikshak"]
    },
]


def search_all(query: str) -> dict:
    """Search across all categories and return matches."""
    query_lower = query.lower()
    results = {"schemes": [], "yojanas": [], "jobs": [], "exams": []}

    for item in SCHEMES:
        if (query_lower in item["name"].lower() or
            query_lower in item["description"].lower() or
            any(query_lower in tag for tag in item["tags"])):
            results["schemes"].append(item)

    for item in YOJANAS:
        if (query_lower in item["name"].lower() or
            query_lower in item["description"].lower() or
            any(query_lower in tag for tag in item["tags"])):
            results["yojanas"].append(item)

    for item in JOBS:
        if (query_lower in item["name"].lower() or
            query_lower in item["description"].lower() or
            any(query_lower in tag for tag in item["tags"])):
            results["jobs"].append(item)

    for item in EXAMS:
        if (query_lower in item["name"].lower() or
            query_lower in item["description"].lower() or
            any(query_lower in tag for tag in item["tags"])):
            results["exams"].append(item)

    return results


def get_item_by_id(item_id: str):
    """Find any item by its ID across all lists."""
    for item in SCHEMES + YOJANAS + JOBS + EXAMS:
        if item["id"] == item_id:
            return item
    return None
