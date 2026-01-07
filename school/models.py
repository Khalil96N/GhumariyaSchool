from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم التصنيف")

    class Meta:
        verbose_name = "تصنيف"
        verbose_name_plural = "تصنيفات"

    def __str__(self):
        return self.name

class Branch(models.Model):
    country = models.CharField(max_length=100, verbose_name="الدولة")
    city = models.CharField(max_length=100, verbose_name="المدينة")
    address = models.TextField(verbose_name="العنوان")
    image = models.ImageField(upload_to='branches/', verbose_name="صورة الفرع", blank=True, null=True)
    bio = models.TextField(verbose_name="نبذة تعريفية")

    class Meta:
        verbose_name = "فرع"
        verbose_name_plural = "فروع"

    def __str__(self):
        return f"{self.country} - {self.city}"

class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="العنوان الرئيسي", default="عن مدرسة الغمارية لإحياء العلوم")
    message = models.TextField(verbose_name="الرسالة")
    objectives = models.TextField(verbose_name="الأهداف (سطر لكل هدف)", help_text="اكتب كل هدف في سطر منفصل")
    logo = models.ImageField(upload_to='about/', verbose_name="شعار المدرسة", blank=True, null=True)
    
    class Meta:
        verbose_name = "صفحة عن المدرسة"
        verbose_name_plural = "صفحة عن المدرسة"
    
    def __str__(self):
        return "محتوى صفحة عن المدرسة"
    
    def get_objectives_list(self):
        """تحويل الأهداف من نص إلى قائمة"""
        return [obj.strip() for obj in self.objectives.split('\n') if obj.strip()]
    
    @classmethod
    def get_instance(cls):
        """الحصول على السجل الوحيد أو إنشاءه"""
        obj, created = cls.objects.get_or_create(
            pk=1,
            defaults={
                'title': 'عن مدرسة الغمارية لإحياء العلوم',
                'message': 'من غزة الصمود، نسعى لإحياء التراث العلمي والشرعي الأصيل على نهج علماء آل الغماري الكرام، لنجمع بين أصالة المنهج ومعاصرة التلقي.',
                'objectives': 'إحياء العلوم المهجورة\nنشر الوعي الشرعي\nبناء جيل يجمع بين العلم والتزكية'
            }
        )
        return obj

class Scholar(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم الشيخ")
    bio = models.TextField(verbose_name="نبذة عن الشيخ", blank=True, null=True)
    image = models.ImageField(upload_to='scholars/', verbose_name="صورة الشيخ", blank=True, null=True)
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الفرع", related_name='scholars')

    class Meta:
        verbose_name = "شيخ"
        verbose_name_plural = "شيوخ"

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الكتاب")
    author = models.CharField(max_length=200, verbose_name="المؤلف", default="مؤلف غير معروف")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, verbose_name="التصنيف")
    description = models.TextField(verbose_name="وصف الكتاب", default="لا يوجد وصف")
    file = models.FileField(upload_to='books/', verbose_name="ملف الكتاب (PDF)", default="default.pdf")
    cover_image = models.ImageField(upload_to='covers/', verbose_name="صورة الغلاف", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "كتاب"
        verbose_name_plural = "كتب"

    def __str__(self):
        return self.title

class Lesson(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان الدرس")
    video_url = models.URLField(verbose_name="رابط الفيديو")
    scholar = models.ForeignKey(Scholar, on_delete=models.CASCADE, related_name='lessons', verbose_name="الشيخ المحاضر")
    branch = models.ForeignKey('Branch', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="الفرع", related_name='lessons')

    class Meta:
        verbose_name = "درس"
        verbose_name_plural = "دروس"

    def __str__(self):
        return self.title
