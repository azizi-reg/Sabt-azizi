import streamlit as st

# تنظیمات اصلی صفحه
st.set_page_config(
    page_title="سامانه هوشمند ثبت عزیزی",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# استایل اختصاصی، حل تداخل فونت و تم تاریک/روشن
st.markdown("""
<style>
    @import url('https://cdn.jsdelivr.net/gh/rastikerdar/vazirmatn@v33.003/Vazirmatn-font-face.css');
    
    /* اعمال فونت و راست‌چین کلی */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3, h4, span, div, label {
        font-family: 'Vazirmatn', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }
    
    /* مخفی‌سازی دکمه پیش‌فرض سایدبار جهت جلوگیری از به هم ریختگی در موبایل */
    [data-testid="stSidebarNav"], [data-testid="collapsedControl"] {
        display: none !important;
    }
    
    /* هدر اصلی */
    .main-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
        color: #ffffff !important;
        padding: 20px;
        border-radius: 12px;
        text-align: center !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    }
    .main-header h2, .main-header p {
        color: #ffffff !important;
        text-align: center !important;
        margin: 5px 0;
    }
    
    /* باکس تماس با کارشناسان */
    .contact-box {
        background: #f8fafc;
        border: 1px solid #cbd5e1;
        border-right: 5px solid #2563eb;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 20px;
        color: #1e293b !important;
    }
    .contact-box p {
        color: #1e293b !important;
        margin: 4px 0;
        font-size: 14px;
    }
    
    /* کارت مدارک و توضیحات با رنگ متن کاملاً مشکی و خوانا */
    .doc-card {
        background-color: #ffffff !important;
        border: 1.5px solid #93c5fd !important;
        border-radius: 10px;
        padding: 18px;
        margin-top: 15px;
        margin-bottom: 15px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    }
    .doc-card h4 {
        color: #1e40af !important;
        font-weight: bold;
        margin-bottom: 12px;
    }
    .doc-card li {
        color: #0f172a !important;
        font-size: 14px !important;
        line-height: 1.9 !important;
        margin-bottom: 6px;
    }
    
    .badge {
        background-color: #dbeafe;
        color: #1d4ed8 !important;
        padding: 3px 10px;
        border-radius: 5px;
        font-size: 12px;
        font-weight: bold;
        display: inline-block;
        margin-bottom: 10px;
    }
    
    .footer {
        text-align: center !important;
        padding: 15px;
        color: #64748b;
        font-size: 12px;
        border-top: 1px solid #e2e8f0;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# هدر بالای صفحه
st.markdown("""
<div class="main-header">
    <h2>⚖️ سامانه خدمات ثبتی عزیزی</h2>
    <p>ثبت شرکت، رتبه‌بندی پیمانکاری (گرید)، ثبت برند و تغییرات شرکتی</p>
</div>
""", unsafe_allow_html=True)

# کارت تماس و اطلاعات سریع
st.markdown("""
<div class="contact-box">
    <p><strong>📞 تلفن همراه کارشناس:</strong> ۰۹۱۲۰۰۰۰۰۰۰</p>
    <p><strong>🏢 دفتر مرکزی:</strong> تهران / یزد</p>
    <p><strong>✉️ ایمیل:</strong> info@sabt-azizi.ir &nbsp;|&nbsp; <strong>⏰ ساعات پاسخگویی:</strong> ۹ الی ۱۷</p>
</div>
""", unsafe_allow_html=True)

# تب‌های سامانه
tab1, tab2, tab3 = st.tabs(["📋 مدارک و خدمات", "📝 ثبت درخواست مشاوره", "ℹ️ درباره ما"])

with tab1:
    st.markdown("### انتخاب خدمت و مشاهده مدارک")
    
    service = st.selectbox(
        "نوع خدمت مورد نظر خود را انتخاب نمایید:",
        [
            "ثبت شرکت (مسئولیت محدود / سهامی خاص)",
            "اخذ و ارتقاء گرید (رتبه) پیمانکاری",
            "ثبت برند و علامت تجاری",
            "تغییرات و تصمیمات شرکت‌ها",
            "کارت بازرگانی و کد اقتصادی"
        ]
    )
    
    if service == "ثبت شرکت (مسئولیت محدود / سهامی خاص)":
        st.markdown("""
        <div class="doc-card">
            <span class="badge">مدارک ثبت شرکت</span>
            <h4>مدارک لازم جهت تاسیس:</h4>
            <ul>
                <li>تصویر کارت ملی و شناسنامه کلیه اعضای هیئت مدیره و سهامداران</li>
                <li>گواهی عدم سوء پیشینه کیفری معتبر برای تمامی اعضا</li>
                <li>انتخاب ۵ نام پیشنهادی (۳ سیلابه با ریشه در فرهنگ دهخدا)</li>
                <li>تعیین آدرس و کد پستی معتبر محل فعالیت شرکت</li>
                <li>مشخص کردن میزان سرمایه اولیه و نسبت سهام هر شریک</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service == "اخذ و ارتقاء گرید (رتبه) پیمانکاری":
        st.markdown("""
        <div class="doc-card">
            <span class="badge">مدارک گرید و رتبه‌بندی</span>
            <h4>مدارک لازم جهت اخذ و ارتقاء رتبه:</h4>
            <ul>
                <li>مدارک کامل ثبتی شرکت (اساسنامه، روزنامه رسمی تاسیس و تغییرات)</li>
                <li>مدارک تحصیلی و شناسنامه‌ای مهندسین امتیازآور شرکت</li>
                <li>گواهی تاییدیه بیمه تأمین اجتماعی پرسنل و کارشناسان</li>
                <li>قراردادها و مفاصاحساب پروژه‌های قبلی (جهت ارتقاء گرید)</li>
                <li>اظهارنامه مالیاتی رسمی دو سال آخر</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service == "ثبت برند و علامت تجاری":
        st.markdown("""
        <div class="doc-card">
            <span class="badge">مالکیت معنوی</span>
            <h4>مدارک لازم جهت ثبت برند:</h4>
            <ul>
                <li>کپی مدارک هویتی متقاضی (یا مدارک شرکتی در صورت ثبت حقوقی)</li>
                <li>طرح گرافیکی لوگو در ابعاد ۱۰×۱۰ سانتی‌متر</li>
                <li>جواز تاسیس، پروانه کسب، پروانه بهره‌برداری یا مجوز فعالیت مرتبط</li>
                <li>کارت بازرگانی معتبر (در صورت وجود حروف لاتین در لوگو یا نام)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service == "تغییرات و تصمیمات شرکت‌ها":
        st.markdown("""
        <div class="doc-card">
            <span class="badge">صورتجلسات تغییرات</span>
            <h4>مدارک لازم جهت ثبت تغییرات:</h4>
            <ul>
                <li>کپی مدارک شناسایی کلیه شرکا و اعضای هیئت مدیره</li>
                <li>آخرین روزنامه رسمی شرکت به همراه لیست سهامداران</li>
                <li>تنظیم و امضای صورتجلسه مجمع عمومی فوق‌العاده یا عادی</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    elif service == "کارت بازرگانی و کد اقتصادی":
        st.markdown("""
        <div class="doc-card">
            <span class="badge">امور بازرگانی</span>
            <h4>مدارک لازم جهت کارت بازرگانی:</h4>
            <ul>
                <li>اصل شناسنامه، کارت ملی و کارت پایان خدمت (برای آقایان)</li>
                <li>سند مالکیت یا اجاره‌نامه با کد رهگیری به نام متقاضی یا شرکت</li>
                <li>گواهی پلمپ دفاتر تجاری سال جاری و گواهی عدم سوء پیشینه</li>
                <li>حساب بانکی معتبر جاری و حداقل سن ۲۳ سال تمام</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.markdown("### فرم درخواست مشاوره")
    st.caption("اطلاعات خود را وارد نمایید تا در اسرع وقت کارشناسان با شما تماس بگیرند.")
    
    with st.form(key="lead_form"):
        name = st.text_input("نام و نام خانوادگی *")
        phone = st.text_input("شماره تلفن همراه *")
        service_type = st.selectbox("موضوع درخواست:", ["ثبت شرکت", "رتبه بندی (گرید)", "ثبت برند", "تغییرات", "سایر"])
        notes = st.text_area("توضیحات اضافی:")
        
        btn = st.form_submit_button("ارسال درخواست مشاوره")
        if btn:
            if name.strip() and phone.strip():
                st.success(f"درخواست شما با موفقیت ثبت شد. به زودی با شماره {phone} تماس خواهیم گرفت.")
            else:
                st.error("لطفاً نام و شماره همراه را تکمیل فرمایید.")

with tab3:
    st.markdown("### درباره خدمات ثبت عزیزی")
    st.write("""
    گروه حقوقی و ثبتی **عزیزی** آماده ارائه خدمات مشاوره‌ای و اجرایی در زمینه‌های:
    - تاسیس انواع شرکت‌های تجاری و موسسات غیرتجاری
    - اخذ رتبه (گرید) پیمانکاری در تمامی رشته‌ها (ابنیه، راه، تاسیسات و...)
    - ثبت علائم تجاری و برند در کمترین زمان ممکن
    """)

st.markdown("""
<div class="footer">
    سامانه هوشمند خدمات ثبتی عزیزی © ۲۰۲۶
</div>
""", unsafe_allow_html=True)
