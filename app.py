import streamlit as st

# ۱. پیکربندی اصلی صفحه
st.set_page_config(
    page_title="ثبت عزیزی | سامانه تخصصی ثبت شرکت و رتبه‌بندی",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ۲. تزریق استایل فوق‌العاده مدرن (CSS)
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');
    
    /* فونت و چیدمان کلی */
    * {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl !important;
    }
    
    /* مخفی‌سازی المنت‌های زائد Streamlit در موبایل */
    #MainMenu, footer, header, [data-testid="stSidebarNav"], [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* پس‌زمینه کلی نرم */
    .stApp {
        background-color: #f8fafc;
    }
    
    /* هدر مدرن با گرادینت و سایه نرم */
    .hero-header {
        background: linear-gradient(135deg, #0f172a 0%, #1e3a8a 50%, #2563eb 100%);
        color: #ffffff !important;
        padding: 30px 20px;
        border-radius: 16px;
        text-align: center !important;
        box-shadow: 0 10px 25px -5px rgba(37, 99, 235, 0.25);
        margin-bottom: 25px;
    }
    .hero-header h1 {
        font-size: 26px !important;
        font-weight: 800 !important;
        color: #ffffff !important;
        margin-bottom: 8px !important;
    }
    .hero-header p {
        font-size: 14px !important;
        color: #cbd5e1 !important;
        margin: 0 !important;
    }
    
    /* کارت‌های شاخص (Metrics) */
    .features-grid {
        display: flex;
        justify-content: space-between;
        gap: 10px;
        margin-bottom: 20px;
    }
    .feature-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 12px 8px;
        text-align: center;
        flex: 1;
        box-shadow: 0 2px 4px rgba(0,0,0,0.02);
    }
    .feature-item span {
        font-size: 20px;
        display: block;
        margin-bottom: 4px;
    }
    .feature-item p {
        font-size: 11px;
        font-weight: bold;
        color: #334155;
        margin: 0;
    }

    /* کارت تماس سریع */
    .contact-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 20px;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
    }
    .contact-title {
        font-size: 15px;
        font-weight: bold;
        color: #1e293b;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        gap: 6px;
    }
    .contact-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 8px 0;
        border-bottom: 1px dashed #f1f5f9;
        font-size: 13.5px;
        color: #475569;
    }
    .contact-row:last-child {
        border-bottom: none;
    }
    
    /* دکمه تماس با استایل */
    .btn-call {
        display: inline-block;
        background: #2563eb;
        color: #ffffff !important;
        padding: 6px 14px;
        border-radius: 8px;
        text-decoration: none !important;
        font-weight: bold;
        font-size: 13px;
        box-shadow: 0 2px 6px rgba(37,99,235,0.3);
        transition: all 0.2s;
    }
    .btn-call:hover {
        background: #1d4ed8;
    }
    
    /* کارت مدارک و توضیحات */
    .doc-box {
        background: #ffffff;
        border: 1px solid #cbd5e1;
        border-right: 5px solid #2563eb;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.04);
    }
    .doc-box h3 {
        color: #1e3a8a !important;
        font-size: 17px !important;
        font-weight: 700;
        margin-bottom: 14px !important;
    }
    .doc-box ul {
        padding-right: 20px;
        margin: 0;
    }
    .doc-box li {
        color: #1e293b !important;
        font-size: 13.5px !important;
        line-height: 2 !important;
        margin-bottom: 4px;
    }
    
    /* فوتر شیک */
    .app-footer {
        text-align: center;
        margin-top: 40px;
        padding: 20px 0 10px 0;
        border-top: 1px solid #e2e8f0;
        color: #94a3b8;
        font-size: 12px;
    }
</style>
""", unsafe_allow_html=True)

# ۳. بنر هدر
st.markdown("""
<div class="hero-header">
    <h1>⚖️ خدمات تخصصی ثبت عزیزی</h1>
    <p>مشاوره و انجام کلیه امور ثبتی، اخذ گرید پیمانکاری و برند تجاری</p>
</div>
""", unsafe_allow_html=True)

# ۴. نوارهای آیکون و قابلیت‌ها
st.markdown("""
<div class="features-grid">
    <div class="feature-item">
        <span>⚡</span>
        <p>سرعت در اجرا</p>
    </div>
    <div class="feature-item">
        <span>📑</span>
        <p>مشاوره تخصصی</p>
    </div>
    <div class="feature-item">
        <span>🤝</span>
        <p>پشتیبانی کامل</p>
    </div>
    <div class="feature-item">
        <span>📍</span>
        <p>دفتر مشهد</p>
    </div>
</div>
""", unsafe_allow_html=True)

# ۵. کارت تماس با دسترسی سریع
st.markdown("""
<div class="contact-card">
    <div class="contact-title">📌 راه‌های ارتباطی و آدرس دفتر:</div>
    <div class="contact-row">
        <span>📞 تماس مستقیم با کارشناس:</span>
        <a href="tel:09120227577" class="btn-call">۰۹۱۲۰۲۲۷۵۷۷</a>
    </div>
    <div class="contact-row">
        <span>🏢 آدرس دفتر:</span>
        <span style="font-weight: 500; color: #1e293b;">مشهد، بین پیامبر اعظم ۱۰ و ۱۲، برج سپهر</span>
    </div>
    <div class="contact-row">
        <span>⏰ ساعت پاسخگویی:</span>
        <span>شنبه تا پنج‌شنبه ۹ الی ۱۸</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ۶. تب‌های اصلی
tab1, tab2, tab3 = st.tabs(["📋 مدارک و راهنما", "📝 درخواست مشاوره", "ℹ️ معرفی و سوابق"])

with tab1:
    service = st.selectbox(
        "خدمت مورد نظر را جهت مشاهده مدارک الزامی انتخاب کنید:",
        [
            "🏢 ثبت شرکت (مسئولیت محدود / سهامی خاص)",
            "🏗️ اخذ و ارتقاء گرید (رتبه) پیمانکاری",
            "🏷️ ثبت برند و لوگوی تجاری",
            "✍️ تغییرات، اساسنامه و تصمیمات شرکت",
            "🌐 کارت بازرگانی و کد اقتصادی"
        ]
    )
    
    if "ثبت شرکت" in service:
        st.markdown("""
        <div class="doc-box">
            <h3>📋 مدارک لازم جهت تاسیس شرکت:</h3>
            <ul>
                <li>تصویر کارت ملی و شناسنامه کلیه اعضای هیئت مدیره و سهامداران</li>
                <li>گواهی عدم سوء پیشینه کیفری برای اعضای اصلی</li>
                <li>ارائه ۵ نام پیشنهادی سه سیلابه و اصیل با ریشه در فرهنگ دهخدا</li>
                <li>آدرس دقیق پستی و کد پستی معتبر به همراه تاییدیه آدرس</li>
                <li>تعیین میزان سرمایه اولیه و نسبت سهام هر شریک</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif "گرید" in service:
        st.markdown("""
        <div class="doc-box">
            <h3>🏗️ مدارک لازم جهت اخذ و ارتقاء رتبه پیمانکاری:</h3>
            <ul>
                <li>اسناد کامل ثبتی شرکت (اساسنامه، اظهارنامه، آخرین روزنامه رسمی)</li>
                <li>مدارک تحصیلی و هویتی مهندسین امتیازآور با سابقه کار مرتبط</li>
                <li>گواهی و تاییدیه سوابق بیمه تأمین اجتماعی مهندسین و پرسنل</li>
                <li>قراردادها، صورت وضعیت‌ها و مفاصاحساب پروژه‌های قبلی</li>
                <li>اظهارنامه مالیاتی رسمی دو سال آخر مالی شرکت</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif "برند" in service:
        st.markdown("""
        <div class="doc-box">
            <h3>🏷️ مدارک لازم جهت ثبت علامت و برند:</h3>
            <ul>
                <li>مدارک هویتی متقاضی (شخص حقیقی) یا اسناد ثبتی (شخص حقوقی)</li>
                <li>نمونه طرح گرافیکی لوگو در ابعاد ۱۰×۱۰ با وضوح بالا</li>
                <li>جواز تاسیس، پروانه کسب، پروانه بهره‌برداری یا مجوز فعالیت مرتبط</li>
                <li>کارت بازرگانی معتبر (تنها در صورتی که نام برند یا لوگو لاتین باشد)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif "تغییرات" in service:
        st.markdown("""
        <div class="doc-box">
            <h3>✍️ مدارک لازم جهت ثبت تغییرات شرکتی:</h3>
            <ul>
                <li>تصویر مدارک هویتی اعضای جدید یا تغییریافته</li>
                <li>آخرین نسخه روزنامه رسمی و لیست سهامداران فعلی</li>
                <li>تنظیم و امضای صورتجلسه مجمع عمومی فوق‌العاده یا عادی به‌طور فوق‌العاده</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif "کارت بازرگانی" in service:
        st.markdown("""
        <div class="doc-box">
            <h3>🌐 مدارک لازم جهت کارت بازرگانی و کد اقتصادی:</h3>
            <ul>
                <li>اصل شناسنامه، کارت ملی و کارت پایان خدمت (آقایان)</li>
                <li>سند مالکیت یا اجاره‌نامه با کد رهگیری به نام متقاضی یا شرکت</li>
                <li>گواهی پلمپ دفاتر سال جاری و عدم سوء پیشینه</li>
                <li>حساب جاری بانکی معتبر و حداقل سن ۲۳ سال تمام</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("##### فرم ثبت اطلاعات و تماس کارشناس")
    with st.form(key="inquiry_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("نام و نام خانوادگی:")
        with col2:
            phone = st.text_input("شماره موبایل:")
            
        topic = st.selectbox("موضوع درخواست:", ["ثبت شرکت", "اخذ گرید پیمانکاری", "ثبت برند و علامت", "تغییرات شرکت", "سایر خدمات"])
        details = st.text_area("توضیحات بیشتر (اختیاری):", placeholder="هرگونه توضیح یا سوال خاصی دارید یادداشت کنید...")
        
        submitted = st.form_submit_button("🚀 ارسال درخواست مشاوره")
        if submitted:
            if name.strip() and phone.strip():
                st.success(f"با تشکر از شما جناب/سرکار {name}، درخواست شما ثبت شد. به زودی با شماره {phone} تماس گرفته خواهد شد.")
            else:
                st.warning("لطفاً نام و شماره تماس خود را وارد نمایید.")

with tab3:
    st.markdown("""
    #### دفتر خدمات ثبتی و رتبه‌بندی عزیزی
    با سال‌ها تجربه تخصصی در زمینه امور حقوقی و شرکتی در استان خراسان رضوی و سراسر کشور:
    
    - **ثبت فوری شرکت‌ها:** تنظیم اصولی اساسنامه و شرکت‌نامه
    - **رتبه‌بندی تخصصی (گرید):** در کلیه رشته‌های ابنیه، راه، تاسیسات، آب و برق
    - **علائم تجاری:** برندینگ و ثبت نام تجاری انحصاری
    
    📍 **محل دفتر:** مشهد، بین پیامبر اعظم ۱۰ و ۱۲، برج سپهر  
    📞 **تلفن تماس:** `09120227577`
    """)

# ۷. فوتر سامانه
st.markdown("""
<div class="app-footer">
    سامانه هوشمند خدمات ثبتی عزیزی © ۲۰۲۶ | طراحی شده جهت تسهیل خدمات ثبتی
</div>
""", unsafe_allow_html=True)
