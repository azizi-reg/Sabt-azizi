import streamlit as st

# تنظیمات اولیه صفحه
st.set_page_config(
    page_title="سامانه هوشمند ثبت عزیزی",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# استایل‌دهی سفارشی، فونت وزیرمتن و راست‌چین (RTL) کامل
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/fonts/webfonts/css/vazirmatn.css');
    
    html, body, [class*="css"], .stMarkdown, .stSelectbox, .stButton, .stTextInput, .stTextArea {
        font-family: 'Vazirmatn', Tahoma, sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        padding: 24px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        color: #ffffff;
        font-size: 26px;
        margin-bottom: 8px;
    }
    
    .main-header p {
        color: #e0e0e0;
        font-size: 15px;
        margin: 0;
    }
    
    .card {
        background-color: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .service-badge {
        display: inline-block;
        padding: 4px 12px;
        background-color: #e0f2fe;
        color: #0369a1;
        border-radius: 20px;
        font-size: 13px;
        font-weight: bold;
        margin-bottom: 12px;
    }
    
    .stButton>button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        font-weight: bold;
        padding: 10px;
        border-radius: 8px;
        border: none;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #1d4ed8;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# هدر اصلی سامانه
st.markdown("""
<div class="main-header">
    <h1>سامانه جامع و هوشمند خدمات ثبت عزیزی</h1>
    <p>مشاوره تخصصی، ثبت شرکت، رتبه‌بندی، تغییرات ثبتی و علائم تجاری با بالاترین دقت و سرعت</p>
</div>
""", unsafe_allow_html=True)

# سایدبار اطلاعات تماس و پشتیبانی
with st.sidebar:
    st.header("📞 ارتباط با کارشناسان")
    st.info("""
    **دفتر مرکزی ثبتی:** تهران / یزد  
    **تلفن پشتیبانی:** ۰۹۱۲۰۰۰۰۰۰۰  
    **ایمیل سازمانی:** info@sabt-azizi.ir  
    **ساعات کاری:** شنبه تا چهارشنبه ۹ الی ۱۷
    """)
    st.markdown("---")
    st.write("🔒 کلیه اطلاعات ارسالی در این سامانه تحت محافظت و محرمانه تلقی می‌گردد.")

# بدنه اصلی
tab1, tab2, tab3 = st.tabs(["📋 خدمات و چک‌لیست مدارک", "📝 ثبت درخواست مشاوره", "ℹ️ درباره ما"])

with tab1:
    st.subheader("انتخاب خدمت و مشاهده مدارک مورد نیاز")
    
    service_type = st.selectbox(
        "نوع خدمت مورد نظر را انتخاب نمایید:",
        [
            "ثبت شرکت با مسئولیت محدود / سهامی خاص",
            "اخذ و ارتقاء گرید (رتبه) پیمانکاری",
            "ثبت برند و علامت تجاری",
            "تغییرات و تصمیمات شرکت‌ها",
            "کارت بازرگانی و کد اقتصادی"
        ]
    )
    
    if service_type == "ثبت شرکت با مسئولیت محدود / سهامی خاص":
        st.markdown("""
        <div class="card">
            <span class="service-badge">تاسیس شرکت</span>
            <h4>مدارک لازم جهت ثبت شرکت:</h4>
            <ul>
                <li>تصویر کارت ملی و شناسنامه کلیه اعضای هیئت مدیره و سهامداران</li>
                <li>گواهی عدم سوء پیشینه کیفری برای کلیه اعضا</li>
                <li>انتخاب ۵ نام پیشنهادی ۳ سیلابه با ریشه فارسی</li>
                <li>تعیین دقیق موضوع فعالیت و آدرس دفتر مرکزی همراه با کد پستی معتبر</li>
                <li>تعیین میزان سرمایه اولیه و درصد سهام هر یک از اعضا</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "اخذ و ارتقاء گرید (رتبه) پیمانکاری":
        st.markdown("""
        <div class="card">
            <span class="service-badge">رتبه‌بندی پیمانکاران (سازمان مدیریت)</span>
            <h4>مدارک لازم جهت اخذ گرید:</h4>
            <ul>
                <li>مدارک کامل ثبتی شرکت (اساسنامه، اظهارنامه/شرکت‌نامه، روزنامه رسمی تاسیس و تغییرات)</li>
                <li>تصویر مدارک هویتی اعضای هیئت مدیره و مهندسین امتیازآور</li>
                <li>کپی مدارک تحصیلی کارشناسی و بالاتر مهندسین به همراه گواهی سابقه بیمه معتبر</li>
                <li>اظهارنامه‌های مالیاتی ۳ سال اخیر به همراه جداول مربوطه</li>
                <li>تصویر قراردادها و مفاصاحساب پروژه‌های اجرایی جهت امتیاز تجربه کاری</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "ثبت برند و علامت تجاری":
        st.markdown("""
        <div class="card">
            <span class="service-badge">مالکیت معنوی</span>
            <h4>مدارک لازم جهت ثبت برند و لوگو:</h4>
            <ul>
                <li>مدارک هویتی متقاضی (شناسنامه و کارت ملی شخص حقیقی یا اسناد شرکت برای شخص حقوقی)</li>
                <li>تصویر شفاف و با کیفیت از نمونه علامت، لوگو یا طرح گرافیکی</li>
                <li>مجوز فعالیت (پروانه کسب، پروانه بهره‌برداری، اینماد یا جواز تاسیس)</li>
                <li>کارت بازرگانی (در صورتی که در نام برند از حروف لاتین استفاده شده باشد)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "تغییرات و تصمیمات شرکت‌ها":
        st.markdown("""
        <div class="card">
            <span class="service-badge">امور مجامع و تغییرات</span>
            <h4>مدارک لازم جهت تنظیم صورتجلسات:</h4>
            <ul>
                <li>تصویر آخرین روزنامه رسمی حاوی اسامی مدیران و دارندگان حق امضا</li>
                <li>لیست کامل سهامداران / شرکا و میزان سهم هر فرد</li>
                <li>مشخصات تغییرات مد نظر (تغییر آدرس، تمدید هیئت مدیره، افزایش/کاهش سرمایه، ورود یا خروج شریک)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "کارت بازرگانی و کد اقتصادی":
        st.markdown("""
        <div class="card">
            <span class="service-badge">امور بازرگانی</span>
            <h4>مدارک لازم:</h4>
            <ul>
                <li>کارت ملی، شناسنامه و حداقل مدرک تحصیلی دیپلم متقاضی / مدیرعامل</li>
                <li>گواهی عدم سوء پیشینه و داشتن حداقل سن ۲۴ سال تمام</li>
                <li>سند مالکیت یا اجاره‌نامه هولوگرام‌دار اداری یا تجاری</li>
                <li>حساب بانکی جاری معتبر با گردش مالی مناسب</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("فرم ارسال مشخصات و درخواست پیگیری")
    with st.form("request_form"):
        col1, col2 = st.columns(2)
        with col1:
            full_name = st.text_input("نام و نام خانوادگی:")
            phone_num = st.text_input("شماره همراه (جهت تماس کارشناس):")
        with col2:
            company_name = st.text_input("نام مجموعه یا شرکت (اختیاری):")
            req_type = st.selectbox("موضوع درخواست:", [
                "مشاوره رایگان تلفنی",
                "ثبت شرکت",
                "اخذ رتبه و گرید",
                "ثبت برند و علامت تجاری",
                "سایر امور ثبتی و حقوقی"
            ])
        
        description = st.text_area("توضیحات تکمیلی یا سوالات شما:")
        submit_btn = st.form_submit_button("ثبت و ارسال درخواست")
        
        if submit_btn:
            if full_name.strip() and phone_num.strip():
                st.success(f"متقاضی گرامی {full_name}، اطلاعات شما با موفقیت ثبت گردید. کارشناسان ما به زودی با شماره {phone_num} تماس خواهند گرفت.")
            else:
                st.error("لطفاً نام و شماره همراه خود را وارد نمایید.")

with tab3:
    st.subheader("درباره گروه خدمات ثبتی عزیزی")
    st.write("""
    مجموعه **ثبت عزیزی** با کادری مجرب از کارشناسان حقوقی و ثبتی، ارائه‌دهنده خدمات تخصصی در زمینه‌های ثبت انواع شرکت‌ها، رتبه‌بندی و اخذ صلاحیت پیمانکاری، ثبت برند و طرح‌های صنعتی، پلمپ دفاتر و تغییرات سازمانی می‌باشد.
    
    هدف ما ارائه خدماتی شفاف، سریع و قانونی با مناسب‌ترین تعرفه برای رونق کسب‌وکار شماست.
    """)

# فوتر
st.markdown("---")
st.caption("تمامی حقوق مادی و معنوی برای سامانه ثبت عزیزی محفوظ است © ۲۰۲۶")
