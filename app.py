import streamlit as st
import base64
import os

# تنظیمات پایه صفحه
st.set_page_config(
    page_title="ثبت عزیزی | سامانه هوشمند خدمات ثبتی",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# تابع بارگذاری و تبدیل عکس به Base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode('utf-8')
    return None

img_base64 = get_image_base64("profile.jpg")

# اگر عکس بود استایل پس‌زمینه با عکس ست می‌شود، در غیر این صورت پس‌زمینه گرادیانت پیش‌فرض
if img_base64:
    hero_bg_style = f"""
        background: linear-gradient(135deg, rgba(15, 23, 42, 0.90) 0%, rgba(30, 41, 59, 0.82) 100%), 
                    url("data:image/jpeg;base64,{img_base64}");
        background-size: cover;
        background-position: center;
    """
    avatar_html = f'<img src="data:image/jpeg;base64,{img_base64}" class="profile-avatar" alt="خانم عزیزی">'
else:
    hero_bg_style = "background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);"
    avatar_html = '<div class="profile-avatar-fallback">⚖️</div>'

# تزریق استایل‌های مدرن و شیک (Vazirmatn & Glassmorphism)
st.markdown(f"""
<style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');
    
    * {{
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
    }}
    
    .stApp {{
        background-color: #0b0f19;
        color: #f8fafc;
    }}
    
    /* هدر لوکس */
    .hero-container {{
        {hero_bg_style}
        border-radius: 24px;
        padding: 40px 30px;
        margin-bottom: 30px;
        border: 1px solid rgba(255, 255, 255, 0.12);
        box-shadow: 0 20px 40px rgba(0,0,0,0.5);
        display: flex;
        align-items: center;
        gap: 25px;
        flex-wrap: wrap;
    }}
    
    .profile-avatar {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid #38bdf8;
        object-fit: cover;
        box-shadow: 0 0 25px rgba(56, 189, 248, 0.4);
    }}
    
    .profile-avatar-fallback {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        border: 4px solid #38bdf8;
        background: #1e293b;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 50px;
    }}
    
    .hero-text h1 {{
        color: #ffffff;
        font-size: 2.2rem;
        font-weight: 800;
        margin: 0 0 10px 0;
        letter-spacing: -0.5px;
    }}
    
    .hero-text p {{
        color: #cbd5e1;
        font-size: 1.1rem;
        margin: 0;
        line-height: 1.6;
    }}
    
    /* کارت‌های شیشه‌ای */
    .glass-card {{
        background: rgba(30, 41, 59, 0.65);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 18px;
        padding: 24px;
        margin-bottom: 20px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.25);
    }}
    
    .badge {{
        background: rgba(56, 189, 248, 0.15);
        color: #38bdf8;
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
        border: 1px solid rgba(56, 189, 248, 0.3);
    }}
    
    /* دکمه‌های فرم و تماس */
    .stButton>button {{
        width: 100%;
        background: linear-gradient(90deg, #0284c7 0%, #0369a1 100%);
        color: white;
        border: none;
        padding: 12px 24px;
        border-radius: 12px;
        font-weight: 700;
        font-size: 1.05rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(2, 132, 199, 0.35);
    }}
    
    .stButton>button:hover {{
        background: linear-gradient(90deg, #0369a1 0%, #075985 100%);
        box-shadow: 0 6px 20px rgba(2, 132, 199, 0.5);
        transform: translateY(-2px);
    }}
    
    .call-btn {{
        display: block;
        text-align: center;
        background: linear-gradient(90deg, #10b981 0%, #059669 100%);
        color: white !important;
        text-decoration: none;
        padding: 14px 20px;
        border-radius: 12px;
        font-weight: 800;
        font-size: 1.1rem;
        margin-top: 15px;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.35);
        transition: all 0.3s ease;
    }}
    
    .call-btn:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 185, 129, 0.5);
    }}
    
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
</style>
""", unsafe_allow_html=True)

# بخش هدر با عکس پرسنلی
st.markdown(f"""
<div class="hero-container">
    {avatar_html}
    <div class="hero-text">
        <span class="badge">مشاوره تخصصی و امور ثبتی</span>
        <h1>سامانه ثبتی خانم عزیزی</h1>
        <p>ثبت انواع شرکت‌ها، برند و علائم تجاری، تغییرات و رتبه‌بندی با بالاترین دقت حقوقی و پیگیری مستقیم</p>
    </div>
</div>
""", unsafe_allow_html=True)

# تب‌بندی محتوا
tab1, tab2, tab3 = st.tabs(["📋 مدارک و راهنمای خدمات", "✍️ ثبت درخواست و مشاوره", "👤 درباره ما و ارتباط"])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("انتخاب نوع خدمت و مشاهده مدارک مورد نیاز")
    
    service = st.selectbox(
        "نوع خدمت درخواستی را مشخص کنید:",
        [
            "ثبت شرکت با مسئولیت محدود",
            "ثبت شرکت سهامی خاص",
            "ثبت برند و نشان تجاری",
            "اخذ کارت بازرگانی",
            "تغییرات و تصمیمات شرکت‌ها",
            "اخذ رتبه و گرید پیمانکاری"
        ]
    )
    
    st.markdown("---")
    
    if service == "ثبت شرکت با مسئولیت محدود":
        st.markdown("""
        **📄 مدارک لازم جهت ثبت شرکت با مسئولیت محدود:**
        1. تصویر شناسنامه و کارت ملی تمامی اعضا و سهامداران
        2. ارائه گواهی عدم سوء پیشینه کیفری برای همه اعضا
        3. مشخص نمودن آدرس دقیق پستی، کد پستی معتبر و شماره تماس ثابت
        4. تعیین سرمایه اولیه شرکت (حداقل ۱,۰۰۰,۰۰۰ ریال)
        5. پیشنهاد ۵ نام ۳ سیلابی دارای ریشه در لغت‌نامه دهخدا
        """)
    elif service == "ثبت شرکت سهامی خاص":
        st.markdown("""
        **📄 مدارک لازم جهت ثبت شرکت سهامی خاص:**
        1. تصویر شناسنامه و کارت ملی اعضای هیئت مدیره و سهامداران (حداقل ۳ نفر)
        2. تصویر شناسنامه و کارت ملی دو نفر بازرس (اصلی و علی‌البدل - نباید نسبت فامیلی داشته باشند)
        3. گواهی افتتاح حساب بانکی و واریز حداقل ۳۵٪ از سرمایه اولیه
        4. گواهی عدم سوء پیشینه برای تمامی مدیران و بازرسان
        5. مشخصات آدرس و ۵ نام پیشنهادی
        """)
    elif service == "ثبت برند و نشان تجاری":
        st.markdown("""
        **📄 مدارک لازم جهت ثبت برند و علامت تجاری:**
        1. تصویر مدارک هویتی متقاضی (شخص حقیقی یا حقوقی)
        2. تصویر مجوز فعالیت (پروانه کسب، اینماد، جواز تاسیس یا پروانه بهره‌برداری)
        3. نمونه فایل لوگو و علامت گرافیکی در ابعاد ۱۰×۱۰ سانتی‌متر
        4. داشتن کارت بازرگانی (در صورتی که برند دارای حروف لاتین باشد)
        """)
    elif service == "اخذ کارت بازرگانی":
        st.markdown("""
        **📄 مدارک لازم اخذ کارت بازرگانی:**
        1. داشتن حداقل ۲۳ سال تمام
        2. اصل مدرک تحصیلی معتبر (حداقل دیپلم)
        3. سند مالکیت یا اجاره‌نامه هولوگرام‌دار به نام متقاضی
        4. کارت پایان خدمت یا معافیت دائم (برای آقایان)
        5. دسته چک صیادی و حساب بانکی فعال
        """)
    elif service == "تغییرات و تصمیمات شرکت‌ها":
        st.markdown("""
        **📄 مدارک لازم تغییرات:**
        1. تصویر آخرین آگهی تأسیس و آخرین آگهی تغییرات رسمی در روزنامه رسمی
        2. مدارک هویتی اعضای جدید هیئت مدیره یا سهامداران
        3. لیست سهامداران و میزان سهم‌الشرکه
        4. صورت‌جلسه تنظیم‌شده مجمع عمومی یا هیئت مدیره
        """)
    elif service == "اخذ رتبه و گرید پیمانکاری":
        st.markdown("""
        **📄 مدارک لازم گرید پیمانکاری:**
        1. مدارک ثبتی کامل شرکت (اساسنامه، اظهارنامه، روزنامه رسمی)
        2. مدارک تحصیلی و سوابق بیمه‌ای مهندسین امتیازآور (حداقل ۳ سال سابقه بیمه مرتبط)
        3. اظهارنامه مالیاتی و جدول قراردادهای ۵ سال اخیر
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("فرم درخواست مشاوره فوری")
    st.write("اطلاعات خود را وارد نمایید تا کارشناسان ما در سریع‌ترین زمان با شما تماس بگیرند.")
    
    with st.form("contact_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("نام و نام خانوادگی:")
        with col2:
            phone = st.text_input("شماره تلفن همراه (جهت تماس):")
            
        service_type = st.selectbox("موضوع درخواست:", ["ثبت شرکت", "ثبت برند", "تغییرات شرکت", "کارت بازرگانی", "رتبه‌بندی", "سایر امور حقوقی"])
        description = st.text_area("توضیحات تکمیلی (اختیاری):")
        
        submit_btn = st.form_submit_button("🚀 ارسال درخواست")
        
        if submit_btn:
            if name.strip() and phone.strip():
                st.success(f"با تشکر جناب/سرکار {name} عزیز، درخواست شما ثبت شد. به زودی با شماره {phone} تماس گرفته خواهد شد.")
            else:
                st.error("لطفاً نام و شماره همراه خود را وارد نمایید.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("ارتباط مستقیم با مدیریت")
    st.write("""
    **خدمات ثبتی عزیزی** با سال‌ها تجربه درخشان در زمینه ثبت انواع شرکت‌ها، برند، علائم تجاری و امور حقوقی شرکت‌ها، همراه مطمئن کسب‌وکار شما از ایده تا ثبت رسمی است.
    """)
    st.markdown("""
    📍 **آدرس دفتر:** تهران، خیابان ولیعصر، برج تجاری و اداری  
    📞 **تلفن مستقیم:** ۰۹۱۲۰۰۰۰۰۰۰  
    ⏰ **ساعات پاسخگویی:** شنبه تا چهارشنبه ۹ ال تشکر جناب/سرکار {name} عزیز، درخواست شما ثبت شد. به زودی با شماره {phone} تماس گرفته خواهد شد.")
            else:
                st.error("لطفاً نام و شماره همراه خود را وارد نمایید.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.subheader("ارتباط مستقیم با مدیریت")
    st.write("""
    **خدمات ثبتی عزیزی** با سال‌ها تجربه درخشان در زمینه ثبت انواع شرکت‌ها، برند، علائم تجاری و امور حقوقی شرکت‌ها، همراه مطمئن کسب‌وکار شما از ایده تا ثبت رسمی است.
    """)
    st.markdown("""
    📍 **آدرس دفتر:** تهران، خیابان ولیعصر، برج تجاری و اداری  
    📞 **تلفن مستقیم:** ۰۹۱۲۰۰۰۰۰۰۰  
    ⏰ **ساعات پاسخگویی:** شنبه تا چهارشنبه ۹ الی ۱۸ | پنجشنبه‌ها ۹ الی ۱۳
    """)
    
    st.markdown("""
    <a href="tel:09120000000" class="call-btn">📞 تماس تلفنی مستقیم جهت مشاوره</a>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
