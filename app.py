import os
import streamlit as st

# تنظیمات اولیه صفحه
st.set_page_config(
    page_title="ثبت عزیزی",
    page_icon="⚖️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# استایل اختصاصی و اصلاح راست‌چین بدون تداخل با منوها
st.markdown("""
<style>
    /* تنظیم فونت و راست‌چین برای متون فارسی بدون دستکاری اجزای داخلی */
    [data-testid="stAppViewContainer"] {
        direction: rtl;
    }

    [data-testid="stMarkdownContainer"] {
        direction: rtl;
        text-align: right;
    }

    [data-testid="stMarkdownContainer"] p, 
    [data-testid="stMarkdownContainer"] h1, 
    [data-testid="stMarkdownContainer"] h2, 
    [data-testid="stMarkdownContainer"] h3 {
        direction: rtl;
        text-align: right;
        line-height: 2;
    }

    /* فیلدهای فرم و متن ورودی */
    input, textarea {
        direction: rtl !important;
        text-align: right !important;
    }

    /* باکس‌های مدارک */
    .doc-item {
        background-color: #f1f5f9;
        color: #1e293b;
        border-right: 4px solid #0284c7;
        border-radius: 6px;
        padding: 12px 14px;
        margin: 8px 0;
        line-height: 1.9;
        text-align: right;
        direction: rtl;
    }

    /* استایل تصویر هدر */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }
    
    [data-testid="stImage"] img {
        border-radius: 50%;
        border: 3px solid #0284c7;
        width: 140px !important;
        height: 140px !important;
        object-fit: cover;
    }
</style>
""", unsafe_allow_html=True)

# یافتن خودکار عکس در مخزن
def find_image():
    for name in ["profile.jpg", "جدید با لباس سفید.jpg", "profile.png", "profile.jpeg"]:
        if os.path.exists(name):
            return name
    for file in os.listdir("."):
        if file.lower().endswith(('.png', '.jpg', '.jpeg')) and not file.startswith('.'):
            return file
    return None

found_img = find_image()

# هدر سایت و نمایش عکس
col1, col2, col3 = st.columns([1, 1.2, 1])
with col2:
    if found_img:
        st.image(found_img)
    else:
        st.markdown("<div style='text-align:center; font-size:60px;'>⚖️</div>", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; margin-bottom: 0px;'>ثبت عزیزی</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748b; margin-top: 5px;'>مشاوره تخصصی و ارائه کلیه خدمات ثبت شرکت‌ها، برند و رتبه‌بندی</p>", unsafe_allow_html=True)
st.markdown("---")

# بانک اطلاعات خدمات
services = {
    "🏢 ثبت شرکت با مسئولیت محدود": {
        "intro": "مناسب فعالیت‌های بازرگانی و خدماتی با حداقل دو شریک و مسئولیت محدود به میزان سرمایه.",
        "docs": [
            ("مدارک هویتی شرکا و مدیران", [
                "تصویر شناسنامه و کارت ملی هوشمند تمامی شرکا و اعضای هیئت‌مدیره",
                "شماره همراه فعال و به نام هر یک از اعضا جهت دریافت پیامک‌های ثبت"
            ]),
            ("مشخصات و اطلاعات شرکت", [
                "ارائه حداقل ۵ نام سه سیلابی فارسی و دارای معنی",
                "تعیین موضوع فعالیت دقیق شرکت",
                "تعیین میزان سرمایه اولیه و سهم‌الشرکه هر یک از شرکا",
                "تعیین سمت مدیران و دارندگان حق امضای مجاز اوراق و اسناد"
            ]),
            ("آدرس و اقامتگاه قانونی", [
                "کدپستی ۱۰ رقمی معتبر به همراه آدرس دقیق پستی دفتر شرکت",
                "شماره تلفن ثابت محل دفتر شرکت"
            ])
        ]
    },
    "🏛️ ثبت شرکت سهامی خاص": {
        "intro": "ساختار رسمی مناسب پروژه‌ها، مناقصات، پیمانکاری و اخذ تسهیلات بانکی.",
        "docs": [
            ("تعداد اعضا و مدارک شناسایی", [
                "حداقل ۳ نفر سهامدار به همراه تصویر شناسنامه و کارت ملی",
                "حداقل ۲ نفر بازرس (اصلی و علی‌البدل) بدون نسبت فامیلی با هیئت‌مدیره",
                "شماره همراه به نام برای تمامی سهامداران و بازرسان"
            ]),
            ("امور مالی و بانکی", [
                "واریز حداقل ۳۵ درصد از سرمایه اولیه به حساب بانکی در شرف تأسیس",
                "تعیین ارزش اسمی هر سهم و تعداد کل سهام"
            ]),
            ("اطلاعات شرکت", [
                "ارائه ۵ نام پیشنهادی سه سیلابی فارسی",
                "تعیین موضوع فعالیت دقیق و آدرس با کد پستی ده‌رقمی"
            ])
        ]
    },
    "™️ ثبت برند و علائم تجاری": {
        "intro": "حمایت قانونی انحصاری از نام تجاری، لوگو و نشان کالاها و خدمات شما.",
        "docs": [
            ("مدارک شخص حقیقی", [
                "تصویر شناسنامه و کارت ملی متقاضی",
                "مجوز فعالیت مرتبط (پروانه کسب، اینماد، جواز تأسیس و...)",
                "کارت بازرگانی (در صورتی که برند حاوی حروف لاتین باشد)"
            ]),
            ("مدارک شخص حقوقی (شرکت)", [
                "روزنامه رسمی آگهی تأسیس و آخرین تغییرات شرکت",
                "مدارک شناسایی دارندگان حق امضا",
                "مجوز فعالیت به نام شرکت",
                "کارت بازرگانی شرکت (برای برندهای دارای لاتین)"
            ]),
            ("مشخصات علامت", [
                "فایل باکیفیت لوگو یا طرح برند",
                "توصیف رنگ‌ها و مفهوم علامت",
                "انتخاب طبقات کالا یا خدمات درخواستی"
            ])
        ]
    },
    "💳 اخذ کارت بازرگانی": {
        "intro": "مجوز رسمی برای امور واردات، صادرات و ترخیص کالا از گمرکات کشور.",
        "docs": [
            ("مدارک هویتی و تحصیلی", [
                "تصویر شناسنامه، کارت ملی و عکس پرسنلی",
                "کارت پایان خدمت یا معافیت برای آقایان",
                "مدرک تحصیلی (حداقل دیپلم) و گواهی عدم سوء‌پیشینه"
            ]),
            ("مدارک مالی و محل فعالیت", [
                "سند مالکیت یا اجاره‌نامه رسمی با کد رهگیری به نام متقاضی یا شرکت",
                "کد اقتصادی و ثبت‌نام در سامانه مالیاتی",
                "گواهی پلمب دفاتر تجاری و داشتن حساب جاری معتبر"
            ])
        ]
    },
    "🔄 تغییرات و صورت‌جلسات شرکت‌ها": {
        "intro": "تمدید هیئت‌مدیره، تغییر آدرس، افزایش/کاهش سرمایه و تغییر موضوع شرکت.",
        "docs": [
            ("مدارک شرکت", [
                "تصویر آگهی تأسیس و آخرین آگهی تغییرات در روزنامه رسمی",
                "اساسنامه یا شرکت‌نامه ثبتی"
            ]),
            ("مشخصات تغییرات", [
                "مدارک شناسایی اعضای جدید یا خارج‌شونده",
                "تعیین موضوع دقیق تصمیمات و نوع جلسه (مجمع یا هیئت‌مدیره)",
                "کد پستی جدید در صورت تغییر آدرس اقامتگاه"
            ])
        ]
    },
    "🏆 اخذ رتبه و گرید پیمانکاری": {
        "intro": "اخذ صلاحیت فنی و مهندسی جهت شرکت در مناقصات بزرگ دولتی.",
        "docs": [
            ("مدارک مهندسین امتیازآور", [
                "مدارک شناسایی و تحصیلی مهندسان عضو",
                "سوابق بیمه مرتبط (۳ تا ۶ سال) متناسب با پایه درخواستی",
                "گواهی‌های اشتغال و قراردادهای کاری"
            ]),
            ("مدارک شرکت و قراردادها", [
                "مدارک ثبتی و اساسنامه شرکت",
                "اظهارنامه‌ها و ترازنامه‌های مالیاتی مصوب",
                "قراردادها و مفاصاحساب‌های پروژه‌های اجرا شده"
            ])
        ]
    }
}

# تب‌بندی صفحات
tab1, tab2, tab3 = st.tabs(["📋 راهنمای مدارک", "📝 ثبت درخواست مشاوره", "📞 ارتباط با ما"])

with tab1:
    st.subheader("راهنمای مدارک لازم")
    st.write("لطفاً خدمت مورد نظر را انتخاب نمایید:")
    
    selected_name = st.selectbox("خدمت ثبتی:", list(services.keys()), label_visibility="collapsed")
    selected_info = services[selected_name]
    
    st.info(selected_info["intro"])
    
    for title, items in selected_info["docs"]:
        with st.expander(f"📌 {title}", expanded=True):
            for itm in items:
                st.markdown(f'<div class="doc-item">✔ {itm}</div>', unsafe_allow_html=True)
                
    st.warning("⚖️ **نکته:** مدارک فوق عمومی هستند و حسب نیاز مراجع ثبتی ممکن است استعلام تکمیلی لازم باشد.")

with tab2:
    st.subheader("فرم درخواست مشاوره فوری")
    st.write("اطلاعات خود را ثبت کنید تا در اسرع وقت برای راهنمایی پرونده با شما تماس بگیریم.")
    
    with st.form("form_consultation", clear_on_submit=True):
        u_name = st.text_input("نام و نام خانوادگی:")
        u_phone = st.text_input("شماره تلفن همراه:")
        u_srv = st.selectbox("نوع درخواست:", list(services.keys()) + ["مشاوره عمومی"])
        u_note = st.text_area("توضیحات بیشتر (اختیاری):", placeholder="شرح کوتاهی از درخواست خود بنویسید...")
        
        btn_send = st.form_submit_button("🚀 ارسال درخواست")
        if btn_send:
            if not u_name.strip() or not u_phone.strip():
                st.error("لطفاً نام و شماره همراه را وارد کنید.")
            else:
                st.success(f"جناب/سرکار {u_name}، درخواست شما با موفقیت ثبت شد. به‌زودی با شماره {u_phone} تماس می‌گیریم.")

with tab3:
    st.subheader("اطلاعات تماس و دفتر")
    st.markdown("""
    <div style="background-color: #f8fafc; padding: 20px; border-radius: 8px; border: 1px solid #cbd5e1; line-height: 2.2;">
        📍 <b>نشانی دفتر:</b> مشهد، برج سپهر<br>
        📞 <b>شماره تماس:</b> جهت هماهنگی و مشاوره<br>
        🕒 <b>ساعات کاری:</b> شنبه تا پنج‌شنبه (ساعات اداری)
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><hr><div style='text-align:center; color:#94a3b8; font-size:0.85rem;'>© کلیه حقوق این سامانه متعلق به <b>ثبت عزیزی</b> است.</div>", unsafe_allow_html=True)
