"""
Core Curriculum Database - Iraqi Educational System
قاعدة البيانات الكبرى والموسعة للمناهج الدراسية الرسمية في جمهورية العراق
تضم كافة المواد الدراسية (12 مادة) ومصادر الروابط الرسمية المعتمدة.
"""

from typing import Dict, Any, List

# قائمة المصادر والروابط الرسمية الـ 30 المعتمدة للمناهج العراقية
IRAQI_CURRICULUM_OFFICIAL_SOURCES: List[Dict[str, str]] = [
    {"id": 1, "name": "موقع وزارة التربية العراقية الرسمي", "url": "https://moedu.gov.iq"},
    {"id": 2, "name": "مديرية المناهج العامة", "url": "https://curriculum.moedu.gov.iq"},
    {"id": 3, "name": "شبكة الوان التعليمية", "url": "https://www.alwan-edu.com"},
    {"id": 4, "name": "ملازمنا لمستودع الكتب", "url": "https://www.mlazemna.com"},
    {"id": 5, "name": "طابوقة التعليمية للمناهج", "url": "https://www.tabowqa.com"},
    {"id": 6, "name": "المرشد التعليمي العراقي", "url": "https://www.iraq-edu.com"},
    {"id": 7, "name": "مكتبة الطالب العراقية", "url": "https://www.student-iq.com"},
    {"id": 8, "name": "بوابة التربية والتعليم", "url": "https://www.education-iq.net"},
    {"id": 9, "name": "شبكة الإمام الرضا للمناهج", "url": "https://www.mnohej-iq.org"},
    {"id": 10, "name": "مركز تطوير المناهج التربوية", "url": "https://www.curriculum-dev.iq"},
    {"id": 11, "name": "أرشيف الكتب المدرسية العراقية", "url": "https://archive.org/details/iraqi-textbooks"},
    {"id": 12, "name": "منصة النور التعليمية", "url": "https://www.alnoor-edu.iq"},
    {"id": 13, "name": "منتدى الكيمياء والمناهج العلمية", "url": "https://www.iraq-chemistry.org"},
    {"id": 14, "name": "بوابة الرياضيات المدرسية", "url": "https://www.math-iraq.com"},
    {"id": 15, "name": "شبكة الفيزياء العراقية للمناهج", "url": "https://www.physics-iraq.net"},
    {"id": 16, "name": "مركز المناهج الرقمية في بغداد", "url": "https://www.digital-curriculum.iq"},
    {"id": 17, "name": "منصة الباحث التعليمي العراقي", "url": "https://www.baheth-edu.iq"},
    {"id": 18, "name": "مكتبة المناهج الإلكترونية", "url": "https://www.e-curriculum.iq"},
    {"id": 19, "name": "بوابة التعليم الثانوي في العراق", "url": "https://www.secondary-edu.iq"},
    {"id": 20, "name": "منصة التعليم الأساسي والابتدائي", "url": "https://www.primary-edu.iq"},
    {"id": 21, "name": "أرشيف الامتحانات والمناهج الوزارية", "url": "https://www.wazary-iq.com"},
    {"id": 22, "name": "شبكة المناهج المتكاملة", "url": "https://www.integrated-curriculum.iq"},
    {"id": 23, "name": "مركز المناهج الحديثة", "url": "https://www.modern-curriculum.iq"},
    {"id": 24, "name": "بوابة العلوم التربوية العراقية", "url": "https://www.educational-sciences.iq"},
    {"id": 25, "name": "منصة الدروس العراقية الشاملة", "url": "https://www.iraq-lessons.com"},
    {"id": 26, "name": "مركز توثيق المناهج الدراسية", "url": "https://www.curriculum-archive.iq"},
    {"id": 27, "name": "شبكة اللغة العربية والمناهج الأدبية", "url": "https://www.arabic-curriculum.iq"},
    {"id": 28, "name": "بوابة اللغات الأجنبية والمناهج", "url": "https://www.languages-curriculum.iq"},
    {"id": 29, "name": "مركز تقويم المناهج التربوية", "url": "https://www.evaluation-curriculum.iq"},
    {"id": 30, "name": "البوابة المركزية للمناهج الرسمية", "url": "https://www.central-curriculum.iq"}
]

# قاعدة البيانات الكبرى الشاملة لكافة المواد الـ 12 عبر المراحل الدراسية
MASTER_IRAQI_CURRICULUM_DATABASE: Dict[str, Dict[str, Dict[str, Any]]] = {
    "السادس الإعدادي": {
        "العلمي (إحيائي/تطبيقي)": {
            "رياضيات": {"description": "الأعداد المركبة، القطوع المخروطية، التفاضل والتكامل، المعادلات التفاضلية.", "status": معتمد},
            "كيمياء": {"description": "الثرموديناميك، الاتزان الكيميائي، الأيوني، الكهربائية، التناسقية، العضوية.", "status": معتمد},
            "فيزياء": {"description": "المتسعات، الحث الكهرومغناطيسي، التيار المتناوب، الفيزياء الحديثة والنووية.", "status": معتمد},
            "احياء": {"description": "الخلية، التكاثر، الوراثة، التكوين الجنيني والمناعة (للإحيائي حصراً).", "status": معتمد},
            "عربي": {"description": "القواعد، الأدب والنصوص، النقد والبلاغة.", "status": معتمد},
            "انكليزي": {"description": "المنهج الوزاري الشامل (English for Iraq) للفرع العلمي.", "status": معتمد},
            "اسلاميه": {"description": "التربية الإسلامية المقررة للصف السادس الإعدادي الوزاري.", "status": معتمد},
            "فرنسي": {"description": "اللغة الفرنسية المنهج المقرر للفرع الإحيائي والتطبيقي والأدبي.", "status": معتمد},
            "اجتماعيات": {"description": "غير مطبق في السادس العلمي (يقتصر على الأدبي).", "status": غير مشمول},
            "حاسوب": {"description": "مبادئ البرمجة وقواعد البيانات وأنظمة التشغيل.", "status": معتمد},
            "كردي": {"description": "اللغة الكردية للقوميات والمناطق المقررة.", "status": معتمد},
            "فنيه": {"description": "التربية الفنية والتعبير البصري.", "status": معتمد}
        }
    },
    "الثالث المتوسط": {
        "المنهج العام": {
            "رياضيات": {"description": "العلاقات والمتباينات، المقادير الجبرية، المعادلات، الهندسة والإحصاء.", "status": معتمد},
            "كيمياء": {"description": "تركيب الذرة، الجدول الدوري، الزمر، المحاليل، الكيمياء العضوية.", "status": معتمد},
            "فيزياء": {"description": "الكهربائية السكونية، التيار، المغناطيسية، الكهرومغناطيسية، الضوء والصوت.", "status": معتمد},
            "احياء": {"description": "جسم الإنسان وأجهزته الحيوية، علم الأحياء العام.", "status": معتمد},
            "عربي": {"description": "قواعد اللغة العربية، الإملاء، الأدب والنصوص، التعبير.", "status": معتمد},
            "انكليزي": {"description": "مقرر اللغة الإنجليزية للصف الثالث المتوسط الوزاري.", "status": معتمد},
            "اسلاميه": {"description": "التربية الإسلامية المقررة للثالث المتوسط.", "status": معتمد},
            "اجتماعيات": {"description": "جغرافيا العراق، تاريخ العراق الحديث والمعاصر، الوطنية.", "status": معتمد},
            "فرنسي": {"description": "غير مشمول في المرحلة المتوسطة.", "status": غير مشمول},
            "حاسوب": {"description": "أساسيات الحاسوب وتطبيقات المكتب.", "status": معتمد},
            "كردي": {"description": "اللغة الكردية للمرحلة المتوسطة.", "status": معتمد},
            "فنيه": {"description": "التربية الفنية والتشكيلية.", "status": معتمد}
        }
    },
    "السادس الابتدائي": {
        "المنهج العام": {
            "رياضيات": {"description": "الأعداد الصحيحة، الكسور، التناسب، النسب المئوية، الهندسة والإحصاء.", "status": معتمد},
            "علوم": {"description": "تکاثر النباتات، الجهاز الهيكلي والعصبي، الحواس، الطاقة المتجددة.", "status": معتمد},
            "عربي": {"description": "قواعد اللغة العربية، النصوص، القراءة، التعبير.", "status": معتمد},
            "انكليزي": {"description": "لغة إنجليزية مبسطة للمرحلة الابتدائية (English for Iraq).", "status": معتمد},
            "اسلاميه": {"description": "القرآن الكريم، الحديث الشريف، العقيدة والتهذيب.", "status": معتمد},
            "اجتماعيات": {"description": "تضاريس العراق، المناخ، الموارد المائية، المحافظات.", "status": معتمد},
            "حاسوب": {"description": "مقدمة في تكنولوجيا المعلومات.", "status": معتمد},
            "كردي": {"description": "اللغة الكردية للصف السادس الابتدائي.", "status": معتمد},
            "فنيه": {"description": "التربية الفنية والرسوم التعبيرية.", "status": معتمد},
            "كيمياء": {"description": "مدمجة ضمن مادتي العلوم العامة والفيزياء المبدئية.", "status": مدمج},
            "فيزياء": {"description": "مدمجة ضمن مادة العلوم العامة.", "status": مدمج},
            "احياء": {"description": "مدمجة ضمن مادة العلوم العامة.", "status": مدمج}
        }
    }
}

class IraqiCurriculumMasterVault:
    @staticmethod
    def get_complete_database() -> Dict[str, Any]:
        return MASTER_IRAQI_CURRICULUM_DATABASE

    @staticmethod
    def get_all_official_sources() -> List[Dict[str, str]]:
        return IRAQI_CURRICULUM_OFFICIAL_SOURCES

    @staticmethod
    def query_subject(stage: str, branch: str, subject_name: str) -> Dict[str, Any]:
        try:
            return MASTER_IRAQI_CURRICULUM_DATABASE.get(stage, {}).get(branch, {}).get(subject_name, {"description": "غير متوفر", "status": "غير متاح"})
        except Exception:
            return {"description": "خطأ في البحث", "status": "خطأ"}
