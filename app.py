import streamlit as st

# تنظیمات اصلی صفحه
st.set_page_config(
    page_title="سامانه هوشمند ثبت عزیزی",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# استایل CSS کامل، واکنش‌گرا و سازگار با حالت تاریک/روشن
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');
    
    * {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl;
        text-align: right;
    }
    
    .main-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #ffffff !important;
        padding: 24px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.15);
    }
    
    .main-header h1, .main-header p {
        color: #ffffff !important;
        text-align: center !important;
    }
    
    /* کارت مدارک با رنگ متن کاملاً واضح و پررنگ */
    .service-card {
        background-color: #ffffff !important;
        color: #111827 !important;
        border: 2px solid #3b82f6 !important;
        border-radius: 12px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
    }
    
    .service-card h4 {
        color: #1e3a8a !important;
        font-weight: 800 !important;
        margin-bottom: 15px !important;
    }
    
    .service-card li {
        color: #1f2937 !important;
        font-size: 15px !important;
        line-height: 1.8 !important;
        font-weight: 500 !important;
    }
    
    .tag {
        background-color: #dbeafe !important;
        color: #1e40af !important;
        padding: 4px 12px;
        border-radius: 6px;
        font-size: 13px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 12px;
    }
    
    .footer {
        text-align: center;
        padding: 20px;
        color: #6b7280;
        font-size: 13px;
        border-top: 1px solid #e5e7eb;
        margin-top: 40px;
    }
</style>
""", unsafe_allow_html=True)

# هدر اصلی سامانه
st.markdown("""
<div class="main-header">
    <h1 style="margin:0; font-size:26px;">⚖️ سامانه جامع و هوشمند خدمات ثبت عزیزی</h1>
    <p style="margin-top:10px; font-size:15px; opacity:0.95;">مرکز تخصصی ثبت شرکت، رتبه‌بندی پیمانکاری (گرید)، تغییرات شرکتی و ثبت علائم تجاری</p>
</div>
""", unsafe_allow_html=True)

# سایدبار ارتباط با کارشناسان
with st.sidebar:
    st.header("📞 ارتباط با کارشناسان")
    st.info("""
    **دفتر مرکزی ثبتی:** تهران / یزد  
    **تلفن پشتیبانی:** ۰۹۱۲۰۰۰۰۰۰۰  
    **ایمیل سازمانی:** info@sabt-azizi.ir  
    **ساعات کاری:** شنبه تا چهارشنبه ۹ الی ۱۷
    """)
    st.divider()
    st.caption("🔒 کلیه اطلاعات ارسالی در این سامانه تحت محافظت و محرمانه تلقی می‌گردد.")

# تب‌بندی بخش‌های سامانه
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
        <div class="service-card">
            <span class="tag">تاسیس شرکت</span>
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
        <div class="service-card">
            <span class="tag">رتبه‌بندی پیمانکاران</span>
            <h4>مدارک لازم جهت اخذ و ارتقاء رتبه:</h4>
            <ul>
                <li>مدارک ثبتی کامل شرکت (اساسنامه، اظهارنامه، روزنامه رسمی تاسیس و آخرین تغییرات)</li>
                <li>مدارک هویتی و تحصیلی مهندسین امتیازآور (حداقل یک نفر با سابقه بیمه مرتبط)</li>
                <li>گواهی سابقه بیمه تأمین اجتماعی پرسنل و مهندسان شرکت</li>
                <li>تصویر موافقت‌نامه، قراردادها و مفاصاحساب پروژه‌های قبلی (برای ارتقاء گرید)</li>
                <li>اظهارنامه مالیاتی و صورت‌های مالی حسابرسی‌شده سال‌های اخیر</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "ثبت برند و علامت تجاری":
        st.markdown("""
        <div class="service-card">
            <span class="tag">مالکیت معنوی</span>
            <h4>مدارک لازم جهت ثبت برند و علامت تجاری:</h4>
            <ul>
                <li>کپی شناسنامه و کارت ملی متقاضی (یا مدارک ثبتی شرکت در صورت ثبت حقوقی)</li>
                <li>نمونه تصویر لوگو و علامت تجاری در ابعاد ۱۰×۱۰ سانتی‌متر</li>
                <li>مجوز فعالیت مرتبط (پروانه بهره‌برداری، جواز تاسیس، پروانه کسب یا کارت بازرگانی)</li>
                <li>کارت بازرگانی (در صورتی که برند دارای حروف لاتین باشد)</li>
                <li>وکالت‌نامه رسمی در صورت پیگیری توسط وکیل قانونی</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "تغییرات و تصمیمات شرکت‌ها":
        st.markdown("""
        <div class="service-card">
            <span class="tag">صورتجلسات و تغییرات</span>
            <h4>مدارک لازم جهت ثبت تغییرات:</h4>
            <ul>
                <li>کپی مدارک هویتی کلیه شرکا، سهامداران و بازرسین</li>
                <li>تصویر آخرین روزنامه رسمی حاوی آخرین هیئت مدیره و سرمایه</li>
                <li>تنظیم و امضای صورتجلسه مجمع عمومی فوق‌العاده یا عادی به‌طور فوق‌العاده</li>
                <li>لیست سهامداران حاضر در جلسه و میزان سهام هر کدام</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service_type == "کارت بازرگانی و کد اقتصادی":
        st.markdown("""
        <div class="service-card">
            <span class="tag">امور مالی و بازرگانی</span>
            <h4>مدارک لازم جهت اخذ کارت بازرگانی:</h4>
            <ul>
                <li>سند مالکیت یا اجاره‌نامه هولوگرام‌دار به نام متقاضی یا شرکت</li>
                <li>گواهی عدم سوء پیشینه و اصل کارت ملی و شناسنامه</li>
                <li>گواهی پلمپ دفاتر تجاری و تاییدیه حساب بانکی جاری</li>
                <li>حداقل سن ۲۳ سال تمام و مدرک تحصیلی مرتبط (حداقل دیپلم)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("درخواست مشاوره تخصصی")
    st.write("لطفاً مشخصات خود را وارد کنید تا کارشناسان ثبت عزیزی با شما تماس بگیرند:")
    
    with st.form(key="consulting_form"):
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("نام و نام خانوادگی *")
            company = st.text_input("نام شرکت / موسسه (اختیاری)")
        with col2:
            phone = st.text_input("شماره تلفن همراه *")
            service_needed = st.selectbox(
                "خدمت درخواستی",
                ["ثبت شرکت", "رتبه‌بندی پیمانکاری", "ثبت برند", "تغییرات شرکتی", "سایر موارد"]
            )
            
        desc = st.text_area("توضیحات تکمیلی یا سوال مورد نظر:")
        submit = st.form_submit_button("ثبت و ارسال درخواست مشاوره")
        
        if submit:
            if name.strip() and phone.strip():
                st.success(f"✅ با تشکر جناب/سرکار {name}، درخواست شما با موفقیت ثبت شد. کارشناسان ما به زودی با شماره {phone} تماس خواهند گرفت.")
            else:
                st.error("⚠️ لطفاً نام و شماره همراه خود را حتماً وارد نمایید.")

with tab3:
    st.subheader("درباره گروه خدمات ثبتی عزیزی")
    st.write("""
    **ثبت عزیزی** با سال‌ها تجربه درخشان در حوزه حقوق تجارت، خدمات ثبتی و رتبه‌بندی، همراه مطمئن کارآفرینان و صاحبان کسب‌وکار در سراسر کشور است.
    
    🎯 **اهداف ما:**
    - ارائه خدمات سریع، شفاف و قانونی
    - ارتقای رتبه و اعتبار شرکت‌های پیمانکاری و مشاور
    - صیانت از برند و نشان تجاری شما
    """)

# فوتر
st.markdown("""
<div class="footer">
    حقوق مادی و معنوی برای سامانه ثبت عزیزی محفوظ است © ۲۰۲۶
</div>
""", unsafe_allow_html=True)
