import sys
from qdlgproxy import (  # type: ignore
    QDlg,
    Text,
    LineEdit,
    Button,
    Table,
    Tr,
    Td,
    Group,
)
from PyQt5.Qt import QApplication


@QDlg("Table test")
def qDlgClass(dlg):
    with Group("Login box"):
        with Table():
            with Tr():
                with Td():
                    Text("Username")
                with Td():
                    username = LineEdit()

            with Tr():
                with Td():
                    Text("Password")
                with Td():
                    password = LineEdit().passwordInput()

            with Tr():
                with Td(colspan=2):
                    (
                        Button("Login")
                        .onClick(lambda: print(username.text(), password.text()))
                        .default()
                    )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    qDlgClass.run()
