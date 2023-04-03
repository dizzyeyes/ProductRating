import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QComboBox
import Comments as co

class Login(QVBoxLayout):
    def __init__(self, parent=None):
        super(Login, self).__init__()
        
        self.username_label = QLabel("Username:", parent=parent)
        self.username_edit = QLineEdit(parent=parent)
        self.password_label = QLabel("Password:", parent=parent)
        self.password_edit = QLineEdit(parent=parent)
        self.password_edit.setEchoMode(QLineEdit.Password)
        
        self.login_button = QPushButton("Login", parent=parent)
        self.addWidget(self.username_label)
        self.addWidget(self.username_edit)
        self.addWidget(self.password_label)
        self.addWidget(self.password_edit)
        self.addWidget(self.login_button)
        
        self.refresh_button = QPushButton("Refresh", parent=parent)
        self.addWidget(self.refresh_button)
        
        self.comment_button = QPushButton("Comment", parent=parent)
        self.addWidget(self.comment_button)
        
    def hide(self):
        self.enable=False

class ListItem(QWidget):
    def __init__(self, i, name, parent=None):
        super(ListItem, self).__init__(parent=parent)

        self.id_label = QLabel(str(i), parent=self)
        self.name_label = QLabel(name, parent=self)
        self.select_box = QComboBox(parent=self)
        self.select_box.addItem("Positive")
        self.select_box.addItem("Negative")
        
        layout = QHBoxLayout()
        layout.addWidget(self.id_label)
        layout.addWidget(self.name_label)
        layout.addWidget(self.select_box)
        self.setLayout(layout)

class ListView(QVBoxLayout):
    def __init__(self, parent=None):
        super(ListView, self).__init__()

        self.list_widget = QListWidget(parent=parent)
        self.addWidget(self.list_widget)

        titles = ["惠寻 京东自有品牌 抽绳垃圾袋45只自动收口加厚塑料袋大号垃圾桶袋",
                "怡宝纯净水1.555L*12瓶/箱大瓶饮用水泡茶整箱",
                "【系列自选】新年过年啦绘本系列 绘本欢乐中国年中华传统节日故事绘本阅读我们的新年",
                "雅诗兰黛绒雾哑光唇膏420#轻奢玫情色口红化妆品礼盒护肤品套装生日礼物"]
                
        for i in range(1, len(titles)):
            item = ListItem(i, titles[i], parent=self.list_widget)
            list_item = QListWidgetItem(self.list_widget)
            list_item.setSizeHint(item.sizeHint())
            self.list_widget.setItemWidget(list_item, item)
            
    def hide(self):
        self.enable=False
        
    def update(self):
        pass

class MainWindow(QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setWindowTitle("Login")
        self.resize(1000, 800)

        self.login_layout = Login(parent=self)
        self.list_view = ListView(parent=self)

        self.main_layout = QVBoxLayout()
        self.main_layout.addLayout(self.login_layout)
        self.main_layout.addLayout(self.list_view)
        self.list_view.hide()

        self.login_layout.login_button.clicked.connect(self.login)
        self.login_layout.refresh_button.clicked.connect(self.refresh)
        self.login_layout.comment_button.clicked.connect(self.comment)
        self.setLayout(self.main_layout)
        self.predictor = co.TextComment()

    def login(self):
        username = self.login_layout.username_edit.text()
        password = self.login_layout.password_edit.text()

        if username == "admin" and password == "password":
            self.login_layout.hide()
            self.list_view.update()
            
    def refresh(self):
        self.list_view.update()
        
    def comment(self):
        for i in range(self.list_view.list_widget.count()):
            item_widget = self.list_view.list_widget.itemWidget(self.list_view.list_widget.item(i))
            title = item_widget.name_label.text()
            status = item_widget.select_box.currentText()
            statusBool = True if item_widget.select_box.currentText() == "Positive" else False
            print(f"商品名称：{title}，选中状态：{status}, {statusBool}")
            comments = self.predictor.comments_gen(title,statusBool)
            print("\n\t评语：\n",comments)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
