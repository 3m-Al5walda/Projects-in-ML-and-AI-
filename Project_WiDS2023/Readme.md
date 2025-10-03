Project_WiDS2023/
├── data/
│   ├── raw/                 # البيانات الأصلية دون تعديل
│   ├── processed/           # البيانات بعد التنظيف والمعالجة
│   └── external/             # مصادر أو بيانات إضافية (إن وجدت)
├── notebooks/
│   └── exploratory_analysis.ipynb    # تحليل استكشافي للبيانات
├── src/
│   ├── preprocessing.py      # دوال التنظيف والمعالجة المسبقة
│   ├── features.py           # دوال استخراج الميزات Feature Engineering
│   ├── modeling.py           # بناء النماذج التدريبية
│   ├── evaluation.py         # دوال تقييم النماذج
│   └── utils.py               # دوال مساعدة عامة
├── outputs/
│   ├── models/               # النماذج المحفوظة (pickle، أو غيرها)
│   ├── predictions/          # نتائج التنبؤ على بيانات الاختبار
│   └── figures/               # الرسوم البيانية والتصورات
├── requirements.txt           # المكتبات المطلوبة (مثل scikit-learn, pandas, numpy, matplotlib…)
└── README.md                  # هذا الملف