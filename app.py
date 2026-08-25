import base64
import os
import streamlit as st


# ==============================
# تنظیمات اولیه صفحه
# ==============================
st.set_page_config(
    page_title="ثبت عزیزی",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ==============================
# توابع کمکی
# ==============================
def image_to_base64(file_path):
    """تبدیل عکس محلی به Base64 برای نمایش پایدار در هدر."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode("utf-8")
    return None


def get_profile_image():
    """یافتن عکس پروفایل با چند نام احتمالی."""
    possible_files = [
        "profile.jpg",
        "profile.png",
        "جدید با لباس سفید.jpg",
        "جدید با لباس سفید.png",
    ]

    for file_name in possible_files:
        image_data = image_to_base64(file_name)
        if image_data:
            extension = file_name.split(".")[-1].lower()
            if extension == "jpg":
                extension = "jpeg"
            return f"data:image/{extension};base64,{image_data}"

    return None


# ==============================
# استایل سایت
# ==============================
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@300;400;500;600;700;800&display=swap');

        * {
            font-family: "Vazirmatn", sans-serif !important;
        }

        .stApp {
            background: linear-gradient(135deg, #0b1220 0%, #111827 50%, #0f172a 100%);
            color: #e2e8f0;
            direction: rtl;
        }

        .block-container {
            max-width: 1200px;
            padding-top: 2rem;
            padding-bottom: 2rem;
        }

        .header-card {
            background: linear-gradient(
                135deg,
                rgba(30, 41, 59, 0.92),
                rgba(15, 23, 42, 0.80)
            );
            border: 1px solid rgba(56, 189, 248, 0.28);
            border-radius: 22px;
            padding: 28px 20px;
            margin-bottom: 25px;
            text-align: center;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.28);
        }

        .profile-frame {
            width: 130px;
            height: 130px;
            padding: 4px;
            margin: 0 auto 15px auto;
            border-radius: 50%;
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.40);
        }

        .profile-img {
            width: 100%;
            height: 100%;
            object-fit: cover;
            border-radius: 50%;
            display: block;
            background: #0f172a;
        }

        .profile-placeholder {
            width: 130px;
            height: 130px;
            margin: 0 auto 15px auto;
            border-radius: 50%;
            display: flex;
            justify-content: center;
            align-items: center;
            font-size: 55px;
            background: linear-gradient(135deg, #0284c7, #4f46e5);
            box-shadow: 0 0 25px rgba(56, 189, 248, 0.35);
        }

        .glass-card {
            background: rgba(30, 41, 59, 0.64);
            border: 1px solid rgba(255, 255, 255, 0.10);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 18px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.18);
        }

        .service-intro {
            border-right: 5px solid #38bdf8;
        }

        .notice-card {
            border-right: 5px solid #f59e0b;
        }

        .check-item {
            padding: 10px 14px;
            margin: 7px 0;
            border-radius: 10px;
            background: rgba(56, 189, 248, 0.08);
            border-right: 3px solid #38bdf8;
            color: #e2e8f0;
            line-height: 1.9;
        }

        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background: rgba(15, 23, 42, 0.70);
            border: 1px solid rgba(255, 255, 255, 0.07);
            padding: 7px;
            border-radius: 14px;
        }

        .stTabs [data-baseweb="tab"] {
            height: 48px;
            border-radius: 10px;
            color: #cbd5e1;
            font-weight: 700;
            background: transparent;
        }

        .stTabs [aria-selected="true"] {
            background: rgba(56, 189, 248, 0.16) !important;
            color: #38bdf8 !important;
            border: 1px solid rgba(56, 189, 248, 0.25) !important;
        }

        .stButton > button,
        .stFormSubmitButton > button {
            width: 100%;
            border: none;
            border-radius: 10px;
            padding: 12px 18px;
            color: white;
            font-weight: 700;
            background: linear-gradient(135deg, #0284c7, #2563eb);
        }

        .stButton > button:hover,
        .stFormSubmitButton > button:hover {
            background: linear-gradient(135deg, #0369a1, #1d4ed8);
        }

        div[data-baseweb="input"] input,
        div[data-baseweb="select"] > div,
        textarea {
            direction: rtl;
            text-align: right;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# ==============================
# هدر
# ==============================
profile_src = get_profile_image()

if profile_src:
    profile_html = f"""
        <div class="profile-frame">
            <img src="{profile_src}" class="profile-img" alt="ثبت عزیزی">
        </div>
    """
else:
    profile_html = """
        <div class="profile-placeholder">⚖️</div>
    """

st.markdown(
    f"""
    <div class="header-card">
        {profile_html}
        <h1 style="color:#ffffff; margin:0 0 8px 0;">ثبت عزیزی</h1>
        <p style="color:#38bdf8; font-size:1.08rem; font-weight:700; margin:0 0 12px 0;">
            مشاوره تخصصی و خدمات جامع ثبتی
        </p>
        <p style="color:#cbd5e1; max-width:760px; margin:0 auto; line-height:2;">
            خدمات ثبت شرکت، ثبت برند و علامت تجاری، تغییرات شرکت‌ها،
            کارت بازرگانی و اخذ رتبه پیمانکاری.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ==============================
# اطلاعات خدمات
# ==============================
service_data = {
    "ثبت شرکت با مسئولیت محدود": {
        "icon": "🏢",
        "intro": "مناسب فعالیت‌های خدماتی، تجاری، بازرگانی و کسب‌وکارهایی که حداقل دو شریک دارند.",
        "sections": [
            (
                "👤 مدارک هویتی شرکا و مدیران",
                [
                    "تصویر واضح کارت ملی تمام شرکا، مدیرعامل و اعضای هیئت‌مدیره",
                    "تصویر تمام صفحات شناسنامه اشخاص",
                    "شماره همراه فعال و آدرس محل سکونت اعضا",
                    "اطلاعات موردنیاز برای احراز هویت و امضای الکترونیکی، در صورت درخواست سامانه",
                ],
            ),
            (
                "📌 اطلاعات ضروری شرکت",
                [
                    "حداقل ۵ نام پیشنهادی فارسی برای شرکت",
                    "تعیین سرمایه اولیه و میزان سهم‌الشرکه هر شریک",
                    "تعیین سمت مدیرعامل، رئیس هیئت‌مدیره و سایر مدیران",
                    "تعیین صاحبان امضای مجاز شرکت",
                    "تعیین موضوع فعالیت، مدت فعالیت و نحوه تقسیم سود",
                ],
            ),
            (
                "📍 آدرس شرکت",
                [
                    "آدرس دقیق محل اقامتگاه قانونی شرکت",
                    "کدپستی ده‌رقمی معتبر",
                    "شماره تلفن ثابت محل شرکت، در صورت نیاز",
                    "اطلاعات سند یا اجاره‌نامه محل، در صورت درخواست پرونده",
                ],
            ),
            (
                "⚠️ نکات مهم",
                [
                    "شرکت با مسئولیت محدود حداقل به دو شریک نیاز دارد.",
                    "نام شرکت نباید تکراری، لاتین یا مغایر ضوابط نام‌گذاری باشد.",
                    "برای موضوعات تخصصی ممکن است مجوز مرجع ذی‌صلاح لازم باشد.",
                ],
            ),
        ],
    },
    "ثبت شرکت سهامی خاص": {
        "icon": "🏛️",
        "intro": "مناسب شرکت‌های پروژه‌محور، پیمانکاری، حضور در مناقصات و کسب‌وکارهای دارای ساختار سهامی.",
        "sections": [
            (
                "👤 مدارک سهامداران، مدیران و بازرسان",
                [
                    "مدارک هویتی حداقل ۳ سهامدار",
                    "مدارک هویتی اعضای هیئت‌مدیره",
                    "مدارک هویتی بازرس اصلی و بازرس علی‌البدل",
                    "اطلاعات تماس و نشانی اشخاص",
                ],
            ),
            (
                "📊 ساختار و سرمایه شرکت",
                [
                    "تعیین میزان سرمایه اولیه شرکت",
                    "تعیین تعداد سهام و سهم هر سهامدار",
                    "تعیین سمت مدیران و صاحبان امضای مجاز",
                    "تعیین بازرس اصلی و بازرس علی‌البدل",
                    "تعیین موضوع فعالیت و مدت شرکت",
                ],
            ),
            (
                "🏦 امور بانکی",
                [
                    "افتتاح حساب به نام شرکت در شرف تأسیس، در صورت نیاز",
                    "واریز سرمایه طبق الزامات پرونده و دریافت گواهی بانکی",
                    "تطبیق اطلاعات بانکی با نام و سرمایه شرکت",
                ],
            ),
            (
                "⚠️ نکات مهم",
                [
                    "شرکت سهامی خاص حداقل ۳ سهامدار و ۲ بازرس نیاز دارد.",
                    "بازرسان نباید عضو هیئت‌مدیره شرکت باشند.",
                    "برای برخی موضوعات فعالیت، ارائه مجوز ضروری است.",
                ],
            ),
        ],
    },
    "ثبت برند و علائم تجاری": {
        "icon": "™️",
        "intro": "برای حمایت قانونی از نام، لوگو، نشان، بسته‌بندی و هویت تجاری کسب‌وکار.",
        "sections": [
            (
                "👤 مدارک شخص حقیقی",
                [
                    "تصویر کارت ملی و شناسنامه متقاضی",
                    "شماره همراه و نشانی معتبر",
                    "مجوز فعالیت مرتبط با کالا یا خدمات",
                    "مدارک تکمیلی لازم در صورت وجود واژه یا حروف لاتین در علامت",
                ],
            ),
            (
                "🏢 مدارک شخص حقوقی",
                [
                    "آگهی تأسیس و آخرین تغییرات شرکت",
                    "مدارک هویتی مدیرعامل یا دارنده حق امضا",
                    "مجوز فعالیت به نام شرکت",
                    "معرفی‌نامه نماینده، در صورت پیگیری توسط نماینده",
                ],
            ),
            (
                "🎨 مدارک مربوط به علامت",
                [
                    "فایل لوگو یا علامت با کیفیت مناسب",
                    "توضیح اجزای نوشتاری و تصویری برند",
                    "تعیین طبقات کالا یا خدمات مورد درخواست",
                    "مشخص‌کردن رنگی یا سیاه‌وسفید بودن علامت",
                ],
            ),
            (
                "⚠️ نکات مهم",
                [
                    "پیش از ثبت، بررسی تشابه برند با علائم پیشین توصیه می‌شود.",
                    "علامت باید قابلیت تمایز داشته باشد.",
                    "علائم گمراه‌کننده یا مغایر مقررات قابل ثبت نیستند.",
                ],
            ),
        ],
    },
    "اخذ کارت بازرگانی": {
        "icon": "💳",
        "intro": "برای فعالیت‌های واردات، صادرات، امور گمرکی و تجارت بین‌المللی.",
        "sections": [
            (
                "👤 مدارک هویتی",
                [
                    "کارت ملی و شناسنامه متقاضی یا مدیرعامل",
                    "شماره همراه فعال و عکس پرسنلی، در صورت نیاز",
                    "مدارک مربوط به وضعیت نظام‌وظیفه برای متقاضیان مشمول",
                    "مدارک تحصیلی یا سوابق مورد نیاز بر اساس شرایط پرونده",
                ],
            ),
            (
                "🏠 مدارک محل فعالیت",
                [
                    "سند مالکیت یا اجاره‌نامه معتبر محل کسب",
                    "کدپستی ده‌رقمی محل فعالیت",
                    "شماره ثابت و نشانی دقیق محل",
                    "مدارک ثبتی شرکت برای درخواست اشخاص حقوقی",
                ],
            ),
            (
                "🏦 امور مالی و اداری",
                [
                    "اطلاعات و وضعیت پرونده مالیاتی",
                    "گواهی‌های بانکی یا مالی در صورت درخواست",
                    "ثبت اطلاعات در سامانه‌های مرتبط",
                    "رفع نقص یا بدهی احتمالی پیش از تکمیل فرآیند",
                ],
            ),
            (
                "⚠️ نکات مهم",
                [
                    "شرایط اشخاص حقیقی و حقوقی با یکدیگر متفاوت است.",
                    "صدور کارت منوط به تأیید مدارک توسط مراجع ذی‌ربط است.",
                    "ممکن است با توجه به وضعیت پرونده، مدارک تکمیلی درخواست شود.",
                ],
            ),
        ],
    },
    "تغییرات و تصمیمات شرکت‌ها": {
        "icon": "🔄",
        "intro": "برای تغییر مدیران، آدرس، موضوع، سرمایه، شرکا، سهامداران و سایر تصمیمات رسمی شرکت.",
        "sections": [
            (
                "📄 مدارک ثبتی شرکت",
                [
                    "آگهی تأسیس شرکت",
                    "آخرین آگهی تغییرات شرکت",
                    "اساسنامه، شرکت‌نامه یا اظهارنامه، حسب نوع شرکت",
                    "شماره ثبت و شناسه ملی شرکت",
                ],
            ),
            (
                "👤 مدارک اشخاص جدید یا خارج‌شونده",
                [
                    "کارت ملی و شناسنامه اعضای جدید",
                    "اطلاعات سمت و حدود اختیارات مدیران جدید",
                    "استعفا، رضایت‌نامه یا مدارک انتقال، در صورت لزوم",
                    "مدارک تکمیلی اشخاص حقوقی، در صورت وجود شریک حقوقی",
                ],
            ),
            (
                "📝 اطلاعات موردنیاز برای صورت‌جلسه",
                [
                    "نوع جلسه و تاریخ برگزاری آن",
                    "موضوع دقیق تغییرات مورد درخواست",
                    "اسامی حاضران و میزان سهم یا سهام آنان",
                    "تصمیمات نهایی و تعیین نماینده پیگیری",
                ],
            ),
            (
                "⚠️ نکات مهم",
                [
                    "نوع صورت‌جلسه باید با نوع تغییر هماهنگ باشد.",
                    "اطلاعات باید بر اساس آخرین وضعیت ثبت‌شده شرکت تنظیم شود.",
                    "برای تغییر آدرس، کدپستی و نشانی کامل جدید لازم است.",
                ],
            ),
        ],
    },
    "اخذ رتبه و گرید پیمانکاری": {
        "icon": "🏆",
        "intro": "برای تکمیل پرونده صلاحیت پیمانکاری و حضور در مناقصات و پروژه‌های مرتبط.",
        "sections": [
            (
                "🏢 مدارک ثبتی شرکت",
                [
                    "آگهی تأسیس و آخرین تغییرات شرکت",
                    "اساسنامه و سایر مدارک ثبتی",
                    "شناسه ملی، شماره ثبت و اطلاعات مدیران",
                    "مدارک محل دفتر شرکت، در صورت نیاز",
                ],
            ),
            (
                "👨‍🔧 مدارک افراد امتیازآور",
                [
                    "مدارک تحصیلی مرتبط افراد امتیازآور",
                    "مدارک هویتی افراد معرفی‌شده",
                    "سوابق بیمه و رزومه کاری مرتبط",
                    "مستندات همکاری یا اشتغال در شرکت، در صورت نیاز",
                ],
            ),
            (
                "💰 سوابق مالی و اجرایی",
                [
                    "قراردادها و سوابق اجرایی شرکت",
                    "گواهی حسن انجام کار یا تأییدیه کارفرما، در صورت وجود",
                    "مدارک مالیاتی، مالی و بیمه‌ای مرتبط",
                    "اطلاعات پروژه‌های پیشین در رشته موردنظر",
                ],
            ),
            (
                "⚠️ نکات مهم",
                [
                    "رشته و پایه درخواستی باید با توان فنی شرکت هماهنگ باشد.",
                    "مدارک و سوابق افراد امتیازآور باید قابل استناد باشند.",
                    "با توجه به رشته و نوع پرونده، مدارک تکمیلی ممکن است لازم شود.",
                ],
            ),
        ],
    },
}


# ==============================
# تب‌ها
# ==============================
tab1, tab2, tab3 = st.tabs(
    ["📋 راهنمای مدارک", "📝 ثبت درخواست مشاوره", "📞 ارتباط با ما"]
)


# ==============================
# تب اول: مدارک
# ==============================
with tab1:
    st.markdown(
        """
        <div class="glass-card">
            <h2 style="color:#38bdf8; margin-top:0;">📋 راهنمای کامل مدارک خدمات</h2>
            <p style="color:#cbd5e1; line-height:2; margin-bottom:0;">
                خدمت موردنظر خود را انتخاب کنید تا مدارک، اطلاعات ضروری و نکات مهم آن نمایش داده شود.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    service_name = st.selectbox(
        "نوع خدمت موردنظر را انتخاب کنید:",
        list(service_data.keys()),
    )

    selected_service = service_data[service_name]

    st.markdown(
        f"""
        <div class="glass-card service-intro">
            <h3 style="color:#ffffff; margin-top:0;">
                {selected_service["icon"]} {service_name}
            </h3>
            <p style="color:#cbd5e1; line-height:2; margin-bottom:0;">
                {selected_service["intro"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    for section_title, items in selected_service["sections"]:
        with st.expander(section_title, expanded=True):
            for item in items:
                st.markdown(
                    f'<div class="check-item">✅ {item}</div>',
                    unsafe_allow_html=True,
                )

    st.markdown(
        """
        <div class="glass-card notice-card">
            <h3 style="color:#fbbf24; margin-top:0;">⚖️ یادآوری مهم</h3>
            <p style="color:#e2e8f0; line-height:2; margin-bottom:0;">
                این فهرست، راهنمای اولیه مدارک است. با توجه به نوع فعالیت، وضعیت اشخاص،
                موضوع شرکت و نظر مرجع مربوط، ممکن است مدارک یا مجوزهای تکمیلی نیز نیاز باشد.
                پیش از ارسال نهایی، پرونده توسط کارشناس بررسی می‌شود.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==============================
# تب دوم: فرم مشاوره
# ==============================
with tab2:
    st.markdown(
        """
        <div class="glass-card">
            <h2 style="color:#38bdf8; margin-top:0;">📝 درخواست مشاوره</h2>
            <p style="color:#cbd5e1; line-height:2; margin-bottom:0;">
                اطلاعات خود را وارد کنید تا برای مشاوره و بررسی اولیه پرونده با شما تماس گرفته شود.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("consultation_form", clear_on_submit=True):
        col1, col2 = st.columns(2)

        with col1:
            full_name = st.text_input("نام و نام خانوادگی")
            phone_number = st.text_input("شماره تلفن همراه")

        with col2:
            request_type = st.selectbox(
                "نوع خدمت",
                list(service_data.keys()) + ["مشاوره تخصصی"],
            )
            city = st.text_input("شهر محل فعالیت")

        description = st.text_area(
            "توضیحات درخواست (اختیاری)",
            placeholder="در صورت تمایل، توضیح کوتاهی درباره درخواست خود بنویسید...",
            height=120,
        )

        submit_request = st.form_submit_button("🚀 ارسال درخواست مشاوره")

        if submit_request:
            if not full_name.strip() or not phone_number.strip():
                st.error("لطفاً نام و نام خانوادگی و شماره تلفن همراه را وارد کنید.")
            else:
                st.success(
                    f"خانم/آقای {full_name}، درخواست شما با موفقیت ثبت شد. "
                    f"برای پیگیری با شماره {phone_number} تماس گرفته خواهد شد."
                )


# ==============================
# تب سوم: تماس
# ==============================
with tab3:
    st.markdown(
        """
        <div class="glass-card" style="text-align:center;">
            <h2 style="color:#38bdf8; margin-top:0;">📞 ارتباط با ثبت عزیزی</h2>
            <p style="color:#cbd5e1; line-height:2;">
                برای مشاوره، پیگیری پرونده و هماهنگی جلسه حضوری از راه‌های زیر اقدام کنید.
            </p>

            <div style="
                background:rgba(15,23,42,0.65);
                border:1px solid rgba(56,189,248,0.22);
                border-radius:14px;
                padding:20px;
                max-width:650px;
                margin:20px auto;
                text-align:right;
                line-height:2.2;
                color:#f1f5f9;
            ">
                <p style="margin:5px 0;">📍 <strong>آدرس دفتر:</strong> مشهد، برج سپهر</p>
                <p style="margin:5px 0;">📞 <strong>تلفن تماس:</strong> شماره تماس خود را در این بخش وارد کنید</p>
                <p style="margin:5px 0;">🕒 <strong>ساعات پاسخ‌گویی:</strong> شنبه تا پنج‌شنبه، ساعات اداری</p>
            </div>

            <p style="color:#94a3b8; font-size:0.9rem;">
                برای فعال‌سازی دکمه تماس مستقیم، شماره تلفن دفتر را در کد جایگزین کنید.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ==============================
# فوتر
# ==============================
st.markdown(
    """
    <div style="
        text-align:center;
        color:#64748b;
        font-size:0.88rem;
        margin-top:35px;
        padding-top:20px;
        border-top:1px solid rgba(255,255,255,0.08);
    ">
        © تمامی حقوق سامانه متعلق به <strong>ثبت عزیزی</strong> است.
    </div>
    """,
    unsafe_allow_html=True,
)
