
// RobControllerDlg.cpp : 實作檔
//

#include "stdafx.h"
#include "RobController.h"
#include "RobControllerDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif

FILE    *fp = NULL;
BOOL    cnt = FALSE;
int     widx = 0, idx = 0, pidx = 0;
char    *saveopen = "C:\\Users\\User\\Desktop\\GripArea\\gripopen.txt";
char    *saveclose = "C:\\Users\\User\\Desktop\\GripArea\\gripclose.txt";
char	*savemove = "C:\\Users\\User\\Desktop\\GripArea\\gripmove.txt";
char    *saveout = "C:\\Users\\User\\Desktop\\Data\\Image.txt";

// 對 App About 使用 CAboutDlg 對話方塊

class CAboutDlg : public CDialogEx
{
public:
	CAboutDlg();

// 對話方塊資料
	enum { IDD = IDD_ABOUTBOX };

	protected:
	virtual void DoDataExchange(CDataExchange* pDX);    // DDX/DDV 支援

// 程式碼實作
protected:
	DECLARE_MESSAGE_MAP()
};

CAboutDlg::CAboutDlg() : CDialogEx(CAboutDlg::IDD)
{
}

void CAboutDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CAboutDlg, CDialogEx)
END_MESSAGE_MAP()


// CRobControllerDlg 對話方塊



CRobControllerDlg::CRobControllerDlg(CWnd* pParent /*=NULL*/)
	: CDialog(CRobControllerDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CRobControllerDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialog::DoDataExchange(pDX);
	DDX_Control(pDX, IDC_CB_AXIS_SEL, m_ComboBox);
	DDX_Control(pDX, IDC_SL_VELOCITY, m_SliderVelocity);
	DDX_Control(pDX, IDC_LIST_NC, m_NCList);
	DDX_Control(pDX, IDC_ED_EDITOR, m_Editor);
	DDX_Control(pDX, IDC_ED_OFFSET_X, m_OffsetX);
	DDX_Control(pDX, IDC_ED_OFFSET_Y, m_OffsetY);
	DDX_Control(pDX, IDC_ED_OFFSET_Z, m_OffsetZ);
	DDX_Control(pDX, IDC_ED_OFFSET_T, m_OffsetT);
	DDX_Control(pDX, IDC_ST_OFFSET, m_ShowOffset);
	DDX_Control(pDX, IDC_LIST_TXT, m_TxtList);
	DDX_Control(pDX, IDC_SL_GSPEED, m_SliderGSpeed);
	DDX_Control(pDX, IDC_SL_GFORCE, m_SliderGForce);
}

BEGIN_MESSAGE_MAP(CRobControllerDlg, CDialog)
	ON_WM_SYSCOMMAND()
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_WM_TIMER()
	ON_WM_LBUTTONDOWN()
	ON_WM_LBUTTONUP()
	ON_WM_HSCROLL()
	ON_BN_CLICKED(IDOK, &CRobControllerDlg::OnBnClickedOk)
	ON_BN_CLICKED(IDCANCEL, &CRobControllerDlg::OnBnClickedCancel)
	ON_BN_CLICKED(IDC_BN_START, &CRobControllerDlg::OnBnClickedBnStart)
	ON_BN_CLICKED(IDC_BN_STOP, &CRobControllerDlg::OnBnClickedBnStop)
	ON_BN_CLICKED(IDC_BN_EXIT, &CRobControllerDlg::OnBnClickedBnExit)
	ON_BN_CLICKED(IDC_BN_SERVO_ON, &CRobControllerDlg::OnBnClickedBnServoOn)
	ON_BN_CLICKED(IDC_BN_SERVO_OFF, &CRobControllerDlg::OnBnClickedBnServoOff)
	ON_EN_CHANGE(IDC_ED_VELOCITY, &CRobControllerDlg::OnEnChangeEdVelocity)
	ON_BN_CLICKED(IDC_BN_HOME, &CRobControllerDlg::OnBnClickedBnHome)
	ON_BN_CLICKED(IDC_BN_MOVE, &CRobControllerDlg::OnBnClickedBnMove)
	ON_BN_CLICKED(IDC_BN_MODE, &CRobControllerDlg::OnBnClickedBnMode)
	ON_BN_CLICKED(IDC_BN_JOINT_CTR, &CRobControllerDlg::OnBnClickedBnJointCtr)
	ON_BN_CLICKED(IDC_BN_P2P_CTR, &CRobControllerDlg::OnBnClickedBnP2pCtr)
	ON_BN_CLICKED(IDC_BN_CP_CTR, &CRobControllerDlg::OnBnClickedBnCpCtr)
	ON_BN_CLICKED(IDC_BN_ENTER, &CRobControllerDlg::OnBnClickedBnEnter)
	ON_BN_CLICKED(IDC_BN_SET_OFFSET, &CRobControllerDlg::OnBnClickedBnSetOffset)
	ON_NOTIFY(LVN_ITEMCHANGED, IDC_LIST_NC, &CRobControllerDlg::OnLvnItemchangedListNc)
	ON_BN_CLICKED(IDC_BN_LOAD, &CRobControllerDlg::OnBnClickedBnLoad)
	ON_BN_CLICKED(IDC_BN_PAINT, &CRobControllerDlg::OnBnClickedBnPaint)
	ON_BN_CLICKED(IDC_BN_GOPEN, &CRobControllerDlg::OnBnClickedBnGopen)
	ON_BN_CLICKED(IDC_BN_GCLOSE, &CRobControllerDlg::OnBnClickedBnGclose)
	ON_BN_CLICKED(IDC_BN_READTXT, &CRobControllerDlg::OnBnClickedBnReadtxt)
	ON_BN_CLICKED(IDC_BN_GMOVE, &CRobControllerDlg::OnBnClickedBnGmove)
	ON_EN_CHANGE(IDC_ED_GSPEED, &CRobControllerDlg::OnEnChangeEdGspeed)
	ON_EN_CHANGE(IDC_ED_GFORCE, &CRobControllerDlg::OnEnChangeEdGforce)
END_MESSAGE_MAP()


// CRobControllerDlg 訊息處理常式

BOOL CRobControllerDlg::OnInitDialog()
{
	CDialog::OnInitDialog();

	// 將 [關於...] 功能表加入系統功能表。

	// IDM_ABOUTBOX 必須在系統命令範圍之中。
	ASSERT((IDM_ABOUTBOX & 0xFFF0) == IDM_ABOUTBOX);
	ASSERT(IDM_ABOUTBOX < 0xF000);

	CMenu* pSysMenu = GetSystemMenu(FALSE);
	if (pSysMenu != NULL)
	{
		BOOL bNameValid;
		CString strAboutMenu;
		bNameValid = strAboutMenu.LoadString(IDS_ABOUTBOX);
		ASSERT(bNameValid);
		if (!strAboutMenu.IsEmpty())
		{
			pSysMenu->AppendMenu(MF_SEPARATOR);
			pSysMenu->AppendMenu(MF_STRING, IDM_ABOUTBOX, strAboutMenu);
		}
	}

	// 設定此對話方塊的圖示。當應用程式的主視窗不是對話方塊時，
	// 框架會自動從事此作業
	SetIcon(m_hIcon, TRUE);			// 設定大圖示
	SetIcon(m_hIcon, FALSE);		// 設定小圖示

	ShowWindow(SW_MINIMIZE);

	// TODO:  在此加入額外的初始設定
	RtxInitialize();

	///////  HMI VALUE INITIALIZE  /////////
	HmiInitialize();

	return TRUE;  // 傳回 TRUE，除非您對控制項設定焦點
}

void CRobControllerDlg::OnSysCommand(UINT nID, LPARAM lParam)
{
	if ((nID & 0xFFF0) == IDM_ABOUTBOX)
	{
		CAboutDlg dlgAbout;
		dlgAbout.DoModal();
	}
	else
	{
		CDialog::OnSysCommand(nID, lParam);
	}
}

// 如果將最小化按鈕加入您的對話方塊，您需要下列的程式碼，
// 以便繪製圖示。對於使用文件/檢視模式的 MFC 應用程式，
// 框架會自動完成此作業。

void CRobControllerDlg::OnPaint()
{
	if (IsIconic())
	{
		CPaintDC dc(this); // 繪製的裝置內容

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 將圖示置中於用戶端矩形
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 描繪圖示
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialog::OnPaint();
	}
}

// 當使用者拖曳最小化視窗時，
// 系統呼叫這個功能取得游標顯示。
HCURSOR CRobControllerDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

void CRobControllerDlg::OnTimer(UINT_PTR nIDEvent)
{
	// TODO:  在此加入您的訊息處理常式程式碼和 (或) 呼叫預設值
	CString strText;

	if (this->misUpdate)
	{
		///////  DISPLAY 6-AXIS ACTUAL POSITION  /////////
		strText.Format(_T("%f"), shv->DisplayActualPos[0]);
		GetDlgItem(IDC_ED_REAL_POS1)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->DisplayActualPos[1]);
		GetDlgItem(IDC_ED_REAL_POS2)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->DisplayActualPos[2]);
		GetDlgItem(IDC_ED_REAL_POS3)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->DisplayActualPos[3]);
		GetDlgItem(IDC_ED_REAL_POS4)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->DisplayActualPos[4]);
		GetDlgItem(IDC_ED_REAL_POS5)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->DisplayActualPos[5]);
		GetDlgItem(IDC_ED_REAL_POS6)->SetWindowText(strText);

		///////  DISPLAY TCP POSITION  /////////
		Forward_Kinematic(shv->DisplayActualPos, &shv->ActualTCP[0], &shv->ActualTOV[0]);

		strText.Format(_T("%f"), shv->ActualTCP[0]);
		GetDlgItem(IDC_ED_REAL_TCPX)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->ActualTCP[1]);
		GetDlgItem(IDC_ED_REAL_TCPY)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->ActualTCP[2]);
		GetDlgItem(IDC_ED_REAL_TCPZ)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->ActualTOV[0]);
		GetDlgItem(IDC_ED_REAL_TOVA)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->ActualTOV[1]);
		GetDlgItem(IDC_ED_REAL_TOVB)->SetWindowText(strText);

		strText.Format(_T("%f"), shv->ActualTOV[2]);
		GetDlgItem(IDC_ED_REAL_TOVC)->SetWindowText(strText);

		if (shv->UIP2PCtr == 1 || shv->UICPCtr == 1)
			ChoosenTOV();
	}

	CDialog::OnTimer(nIDEvent);
}

void CRobControllerDlg::OnBnClickedOk()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	//CDialog::OnOK();
}

void CRobControllerDlg::OnBnClickedCancel()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	//CDialog::OnCancel();
}

void CRobControllerDlg::OnBnClickedBnStart()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	this->misUpdate = 1;

	GetDlgItem(IDC_BN_START)->EnableWindow(false);
	GetDlgItem(IDC_BN_EXIT)->EnableWindow(false);
	GetDlgItem(IDC_BN_STOP)->EnableWindow(true);
	GetDlgItem(IDC_BN_SERVO_ON)->EnableWindow(true);

	CommunicationInit();
	SetTCPOffset(tcpoffset);

	AfxBeginThread(WriteProc, this, THREAD_PRIORITY_ABOVE_NORMAL);
}

void CRobControllerDlg::OnBnClickedBnStop()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_EXIT)->EnableWindow(true);
	GetDlgItem(IDC_BN_START)->EnableWindow(false);
	GetDlgItem(IDC_BN_STOP)->EnableWindow(false);
	GetDlgItem(IDC_BN_SERVO_ON)->EnableWindow(false);

	shv->UIStop = 1;
}

void CRobControllerDlg::OnBnClickedBnExit()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	OpenGrip = FALSE;

	if (AfxMessageBox("Did you press STOP button?!", MB_ICONQUESTION | MB_YESNOCANCEL) == IDYES)
	{
		CDialog::OnCancel();
	}	
}

void CRobControllerDlg::OnBnClickedBnServoOn()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_SERVO_ON)->EnableWindow(false);
	GetDlgItem(IDC_BN_STOP)->EnableWindow(false);
	GetDlgItem(IDC_BN_SERVO_OFF)->EnableWindow(true);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(true);
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(true);
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(true);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(true);
	GetDlgItem(IDC_CB_AXIS_SEL)->EnableWindow(true);
	GetDlgItem(IDC_BN_JOG_P)->EnableWindow(true);
	GetDlgItem(IDC_BN_JOG_N)->EnableWindow(true);
	GetDlgItem(IDC_SL_VELOCITY)->EnableWindow(true);
	GetDlgItem(IDC_ED_VELOCITY)->EnableWindow(true);
	GetDlgItem(IDC_ED_OFFSET_X)->EnableWindow(true);
	GetDlgItem(IDC_ED_OFFSET_Y)->EnableWindow(true);
	GetDlgItem(IDC_ED_OFFSET_Z)->EnableWindow(true);
	GetDlgItem(IDC_ED_OFFSET_T)->EnableWindow(true);
	GetDlgItem(IDC_BN_SET_OFFSET)->EnableWindow(true);
	GetDlgItem(IDC_BN_LOAD)->EnableWindow(true);
	GetDlgItem(IDC_BN_ENTER)->EnableWindow(true);

	shv->UIServoOnOff = 1;
}

void CRobControllerDlg::OnBnClickedBnServoOff()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_MODE)->EnableWindow(false);
	GetDlgItem(IDC_BN_MOVE)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS1)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS2)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS3)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS4)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS5)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS6)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPX)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPY)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPZ)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVA)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVB)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVC)->EnableWindow(false);
	GetDlgItem(IDC_BN_SERVO_OFF)->EnableWindow(false);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(false);
	GetDlgItem(IDC_CB_AXIS_SEL)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOG_P)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOG_N)->EnableWindow(false);
	GetDlgItem(IDC_SL_VELOCITY)->EnableWindow(false);
	GetDlgItem(IDC_ED_VELOCITY)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_X)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_Y)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_Z)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_T)->EnableWindow(false);
	GetDlgItem(IDC_BN_SET_OFFSET)->EnableWindow(false);
	GetDlgItem(IDC_BN_LOAD)->EnableWindow(false);
	GetDlgItem(IDC_BN_PAINT)->EnableWindow(false);
	GetDlgItem(IDC_BN_ENTER)->EnableWindow(false);
	GetDlgItem(IDC_BN_STOP)->EnableWindow(true);
	GetDlgItem(IDC_BN_SERVO_ON)->EnableWindow(true);

	shv->UIServoOnOff = 2;
}

void CRobControllerDlg::OnLButtonDown(UINT nFlags, CPoint point)
{
	// TODO:  在此加入您的訊息處理常式程式碼和 (或) 呼叫預設值

	CDialog::OnLButtonDown(nFlags, point);
}

void CRobControllerDlg::OnLButtonUp(UINT nFlags, CPoint point)
{
	// TODO:  在此加入您的訊息處理常式程式碼和 (或) 呼叫預設值

	CDialog::OnLButtonUp(nFlags, point);
}

BOOL CRobControllerDlg::PreTranslateMessage(MSG* pMsg)
{
	// TODO:  在此加入特定的程式碼和 (或) 呼叫基底類別
	int iden;

	
	////   JOG CONTROL   ////
	if (pMsg->message == WM_LBUTTONDOWN && pMsg->hwnd == ((CButton*)this->GetDlgItem(IDC_BN_JOG_P))->m_hWnd)
	{
		shv->UIAxisSel = m_ComboBox.GetCurSel();
		shv->UIJog = 1;  //Positive
	}

	if (pMsg->message == WM_LBUTTONUP && pMsg->hwnd == ((CButton*)this->GetDlgItem(IDC_BN_JOG_P))->m_hWnd)
	{
		shv->UIJog = 0;//Negative
	}

	if (pMsg->message == WM_LBUTTONDOWN && pMsg->hwnd == ((CButton*)this->GetDlgItem(IDC_BN_JOG_N))->m_hWnd)
	{
		shv->UIAxisSel = m_ComboBox.GetCurSel();
		shv->UIJog = 2;  //Positive
	}

	if (pMsg->message == WM_LBUTTONUP && pMsg->hwnd == ((CButton*)this->GetDlgItem(IDC_BN_JOG_N))->m_hWnd)
	{
		shv->UIJog = 0;//Negative
		
	}
	

	////   NC-EDITOR LIST   ////
	if (pMsg->message == WM_KEYDOWN)
	{
		if (pMsg->wParam == VK_RETURN)
		{
			pos = m_NCList.GetSelectionMark();
			iden = m_NCList.InsertColumn(pos + 1, "");
			return TRUE;
		}
		if (pMsg->wParam == VK_ESCAPE)
			return TRUE;
	}
	return CDialog::PreTranslateMessage(pMsg);
}

void CRobControllerDlg::OnEnChangeEdVelocity()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	CString str;
	int velpos;

	GetDlgItemText(IDC_ED_VELOCITY, str);
	velpos = _ttoi(str);
	m_SliderVelocity.SetPos(velpos);

	shv->Velcity = velpos;
}

void CRobControllerDlg::OnEnChangeEdGspeed()
{
	CString str;
	int velpos;

	GetDlgItemText(IDC_ED_GSPEED, str);
	velpos = _ttoi(str);
	m_SliderGSpeed.SetPos(velpos);

	shv->GSpeed1 = velpos;
}

void CRobControllerDlg::OnEnChangeEdGforce()
{
	CString str;
	int velpos;

	GetDlgItemText(IDC_ED_GFORCE, str);
	velpos = _ttoi(str);
	m_SliderGForce.SetPos(velpos);

	shv->GForce1 = velpos;
}

void CRobControllerDlg::OnHScroll(UINT nSBCode, UINT nPos, CScrollBar* pScrollBar)
{
	// TODO:  在此加入您的訊息處理常式程式碼和 (或) 呼叫預設值
	int editvel; CString str;

	CSliderCtrl *pSlidCtrl1 = (CSliderCtrl*)GetDlgItem(IDC_SL_GSPEED);
	editvel = pSlidCtrl1->GetPos();
	str.Format("%d", editvel);
	SetDlgItemText(IDC_ED_GSPEED, str);

	shv->GSpeed1 = editvel;

	CSliderCtrl *pSlidCtrl2 = (CSliderCtrl*)GetDlgItem(IDC_SL_GFORCE);
	editvel = pSlidCtrl2->GetPos();
	str.Format("%d", editvel);
	SetDlgItemText(IDC_ED_GFORCE, str);

	shv->GForce1 = editvel;

	/******************************************************************/

	CSliderCtrl *pSlidCtrl = (CSliderCtrl*)GetDlgItem(IDC_SL_VELOCITY);
	editvel = pSlidCtrl->GetPos();

	str.Format("%d", editvel);
	SetDlgItemText(IDC_ED_VELOCITY, str);

	shv->Velcity = editvel;

	CDialog::OnHScroll(nSBCode, nPos, pScrollBar);
}

void CRobControllerDlg::OnBnClickedBnHome()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	//double home[6] = { 0.0, 0.0, 90.0, 0.0, 0.0, 0.0 };
	double home[6] = { 90.0, 0.0, 0.0, 0.0, -90.0, 0.0 };

	for (int i = 0; i < TOTAL_AXES; i++)
	{
		shv->MovingPos[i] = home[i];
	}

	shv->UIMove = 1;
}

void CRobControllerDlg::OnBnClickedBnMove()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	CString joint_str[6], tcp_str[3], tov_str[3], strText;
	int  ctov;

	if (shv->UIJointCtr == 1)
	{
		GetDlgItemText(IDC_ED_POS1, joint_str[0]);
		GetDlgItemText(IDC_ED_POS2, joint_str[1]);
		GetDlgItemText(IDC_ED_POS3, joint_str[2]);
		GetDlgItemText(IDC_ED_POS4, joint_str[3]);
		GetDlgItemText(IDC_ED_POS5, joint_str[4]);
		GetDlgItemText(IDC_ED_POS6, joint_str[5]);

		for (int i = AXIS1; i < TOTAL_AXES; i++)
			shv->MovingPos[i] = atof(joint_str[i]);

		shv->UIMove = 1;
	}
	else if (shv->UIP2PCtr == 1)
	{

		GetDlgItemText(IDC_ED_TCPX, tcp_str[0]);
		GetDlgItemText(IDC_ED_TCPY, tcp_str[1]);
		GetDlgItemText(IDC_ED_TCPZ, tcp_str[2]);
		GetDlgItemText(IDC_ED_TOVA, tov_str[0]);
		GetDlgItemText(IDC_ED_TOVB, tov_str[1]);
		GetDlgItemText(IDC_ED_TOVC, tov_str[2]);

		for (int i = X; i < TOTAL_TCP; i++)
			shv->MovingTCP[i] = atof(tcp_str[i]) + tcpoffset[i];

		for (int i = AFA; i < TOTAL_TOV; i++)
			shv->MovingTOV[i] = atof(tov_str[i]);

		shv->UIMove = 1;
	}
	else if (shv->UICPCtr == 1)
	{
		GetDlgItemText(IDC_ED_TCPX, tcp_str[0]);
		GetDlgItemText(IDC_ED_TCPY, tcp_str[1]);
		GetDlgItemText(IDC_ED_TCPZ, tcp_str[2]);
		GetDlgItemText(IDC_ED_TOVA, tov_str[0]);
		GetDlgItemText(IDC_ED_TOVB, tov_str[1]);
		GetDlgItemText(IDC_ED_TOVC, tov_str[2]);

		for (int i = X; i < TOTAL_TCP; i++)
			shv->MovingTCP[i] = atof(tcp_str[i]) + tcpoffset[i];

		for (int i = AFA; i < TOTAL_TOV; i++)
			shv->MovingTOV[i] = atof(tov_str[i]);

		shv->UIMove = 2;
	}
}

void CRobControllerDlg::OnBnClickedBnMode()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_MODE)->EnableWindow(false);
	GetDlgItem(IDC_BN_MOVE)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS1)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS2)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS3)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS4)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS5)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS6)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPX)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPY)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPZ)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVA)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVB)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVC)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(true);
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(true);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(true);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(true);

	shv->UIJointCtr = 0;
	shv->UIP2PCtr = 0;
	shv->UICPCtr = 0;
}

void CRobControllerDlg::OnBnClickedBnJointCtr()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS1)->EnableWindow(true);
	GetDlgItem(IDC_ED_POS2)->EnableWindow(true);
	GetDlgItem(IDC_ED_POS3)->EnableWindow(true);
	GetDlgItem(IDC_ED_POS4)->EnableWindow(true);
	GetDlgItem(IDC_ED_POS5)->EnableWindow(true);
	GetDlgItem(IDC_ED_POS6)->EnableWindow(true);
	GetDlgItem(IDC_BN_MOVE)->EnableWindow(true);
	GetDlgItem(IDC_BN_MODE)->EnableWindow(true);

	shv->UIJointCtr = 1;
}

void CRobControllerDlg::OnBnClickedBnP2pCtr()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPX)->EnableWindow(true);
	GetDlgItem(IDC_ED_TCPY)->EnableWindow(true);
	GetDlgItem(IDC_ED_TCPZ)->EnableWindow(true);
	GetDlgItem(IDC_BN_MOVE)->EnableWindow(true);
	GetDlgItem(IDC_BN_MODE)->EnableWindow(true);

	shv->UIP2PCtr = 1;
}

void CRobControllerDlg::OnBnClickedBnCpCtr()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPX)->EnableWindow(true);
	GetDlgItem(IDC_ED_TCPY)->EnableWindow(true);
	GetDlgItem(IDC_ED_TCPZ)->EnableWindow(true);
	GetDlgItem(IDC_BN_MOVE)->EnableWindow(true);
	GetDlgItem(IDC_BN_MODE)->EnableWindow(true);

	shv->UICPCtr = 1;
}

void CRobControllerDlg::OnBnClickedBnEnter()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	pos = m_NCList.GetSelectionMark();
	m_Editor.GetWindowText(editor);
	m_NCList.SetItemText(pos, 0, editor + "\n");
}

void CRobControllerDlg::OnBnClickedBnSetOffset()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	CString offset_str[4], show_offset;

	m_OffsetX.GetWindowText(offset_str[X]);
	tcpoffset[X] = atof(offset_str[X]);
	m_OffsetY.GetWindowText(offset_str[Y]);
	tcpoffset[Y] = atof(offset_str[Y]);
	m_OffsetZ.GetWindowText(offset_str[Z]);
	tcpoffset[Z] = atof(offset_str[Z]);
	m_OffsetT.GetWindowText(offset_str[TOOL]);
	tcpoffset[TOOL] = atof(offset_str[TOOL]);

	SetTCPOffset(tcpoffset);

	show_offset.Format("%.3f\n\n%.3f\n\n%.3f\n\n%.3f", tcpoffset[X], tcpoffset[Y], tcpoffset[Z], tcpoffset[TOOL]);
	m_ShowOffset.SetWindowTextA(show_offset);
}

void CRobControllerDlg::OnLvnItemchangedListNc(NMHDR *pNMHDR, LRESULT *pResult)
{
	LPNMLISTVIEW pNMLV = reinterpret_cast<LPNMLISTVIEW>(pNMHDR);
	// TODO:  在此加入控制項告知處理常式程式碼
	pos = m_NCList.GetSelectionMark();
	editor = m_NCList.GetItemText(pos, 0);
	m_Editor.SetWindowText(editor);
	*pResult = 0;
}

void CRobControllerDlg::OnBnClickedBnLoad()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_PAINT)->EnableWindow(true);

	LPCTSTR szFilter = _T("Interpolator File(*.hrb)|*.hrb|All File(*.*)|*.*||");
	CFileDialog FileOpenDlg(TRUE, NULL, NULL, OFN_HIDEREADONLY, szFilter, this);

	if (FileOpenDlg.DoModal() == IDOK)
	{
		fPath = FileOpenDlg.GetPathName();
		ext = FileOpenDlg.GetFileExt();
		if (ext == "hrb")	SetNCEditor(fPath);
		else	AfxMessageBox("Wrong!");
	}
	else
	{
		AfxMessageBox("Not load file");
		return;
	}
	return;
}

void CRobControllerDlg::OnBnClickedBnPaint()
{
	// TODO:  在此加入控制項告知處理常式程式碼
	GetDlgItem(IDC_BN_PAINT)->EnableWindow(false);
	PM2NFU();
	BLKgeometrics();
	shv->UIPaint = 1;
}

void CRobControllerDlg::OnBnClickedBnGopen()
{
	shv->GOpen = TRUE;
}

void CRobControllerDlg::OnBnClickedBnGclose()
{
	shv->GClose = TRUE;
}

void CRobControllerDlg::OnBnClickedBnGmove()
{
	CString x;
	GetDlgItemText(IDC_ED_GPOS, x);
	shv->GPosition = atoi(x);
	shv->GSpeed = shv->GSpeed1;
	shv->GForce = shv->GForce1;
	shv->GMove = TRUE;
}

void CRobControllerDlg::OnBnClickedBnReadtxt()
{
	txtstart = TRUE;
	breakpoint = FALSE;
	AfxBeginThread(WriteProc1, this, THREAD_PRIORITY_ABOVE_NORMAL); //Work, WriteProc
}

void CRobControllerDlg::RtxInitialize()
{
	if (CreateSharedMemory() == TRUE)
	{
		ret = NEC_LoadRtxApp("C:\\src\\RobController\\x64\\RtssDebug\\RobRtssApp.rtss");
		if (ret != 0) MessageBox("Load RobRtssApp.rtss faild!");

		UnitConversion();
	}
	Sleep(2000);
}

void CRobControllerDlg::HmiInitialize()
{
	CString str, show_offset;
	CFont m_ListFont;
	CRect rect;
	static int first = 1;
	initvel = 10;
	searchtxt = 0;
	txtstart = TRUE;

	this->misUpdate = 0;
	this->TimerHandle = SetTimer(NULL, 100, NULL);

	GetDlgItem(IDC_BN_START)->EnableWindow(true);
	GetDlgItem(IDC_BN_EXIT)->EnableWindow(true);
	GetDlgItem(IDC_BN_STOP)->EnableWindow(false);
	GetDlgItem(IDC_BN_SERVO_ON)->EnableWindow(false);
	GetDlgItem(IDC_BN_SERVO_OFF)->EnableWindow(false);
	GetDlgItem(IDC_BN_HOME)->EnableWindow(false);
	GetDlgItem(IDC_CB_AXIS_SEL)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOG_P)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOG_N)->EnableWindow(false);
	GetDlgItem(IDC_SL_VELOCITY)->EnableWindow(false);
	GetDlgItem(IDC_ED_VELOCITY)->EnableWindow(false);
	GetDlgItem(IDC_BN_JOINT_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_P2P_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_CP_CTR)->EnableWindow(false);
	GetDlgItem(IDC_BN_MOVE)->EnableWindow(false);
	GetDlgItem(IDC_BN_MODE)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS1)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS2)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS3)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS4)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS5)->EnableWindow(false);
	GetDlgItem(IDC_ED_POS6)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPX)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPY)->EnableWindow(false);
	GetDlgItem(IDC_ED_TCPZ)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVA)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVB)->EnableWindow(false);
	GetDlgItem(IDC_ED_TOVC)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_X)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_Y)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_Z)->EnableWindow(false);
	GetDlgItem(IDC_ED_OFFSET_T)->EnableWindow(false);
	GetDlgItem(IDC_BN_SET_OFFSET)->EnableWindow(false);
	GetDlgItem(IDC_BN_LOAD)->EnableWindow(false);
	GetDlgItem(IDC_BN_PAINT)->EnableWindow(false);
	GetDlgItem(IDC_BN_ENTER)->EnableWindow(false);

	SetDlgItemText(IDC_ED_POS1, "0.0");
	SetDlgItemText(IDC_ED_POS2, "0.0");
	SetDlgItemText(IDC_ED_POS3, "90.0");
	SetDlgItemText(IDC_ED_POS4, "0.0");
	SetDlgItemText(IDC_ED_POS5, "0.0");
	SetDlgItemText(IDC_ED_POS6, "0.0");

	SetDlgItemText(IDC_ED_TCPX, "-10.0");
	SetDlgItemText(IDC_ED_TCPY, "0.0");
	SetDlgItemText(IDC_ED_TCPZ, "1189.5");
	SetDlgItemText(IDC_ED_TOVA, "180.0");
	SetDlgItemText(IDC_ED_TOVB, "0.0");
	SetDlgItemText(IDC_ED_TOVC, "0.0");

	m_ComboBox.InsertString(AXIS1, "Axis1");
	m_ComboBox.InsertString(AXIS2, "Axis2");
	m_ComboBox.InsertString(AXIS3, "Axis3");
	m_ComboBox.InsertString(AXIS4, "Axis4");
	m_ComboBox.InsertString(AXIS5, "Axis5");
	m_ComboBox.InsertString(AXIS6, "Axis6");
	//NEW
	m_ComboBox.InsertString(TCPX, "TCPX");
	m_ComboBox.InsertString(TCPY, "TCPY");
	m_ComboBox.InsertString(TCPZ, "TCPZ");

	m_SliderVelocity.SetRange(0, 100);
	m_SliderVelocity.SetPos(initvel);
	str.Format("%d", initvel);
	SetDlgItemText(IDC_ED_VELOCITY, str);

	m_SliderGSpeed.SetRange(0, 100);
	m_SliderGSpeed.SetPos(0);
	SetDlgItemText(IDC_SL_GSPEED, "0");

	m_SliderGForce.SetRange(0, 100);
	m_SliderGForce.SetPos(0);
	SetDlgItemText(IDC_SL_GFORCE, "0");

	SetDlgItemText(IDC_ED_GDELAY, "3.0");

	m_NCList.SetFont(&m_ListFont);

	for (int i = X; i <= Z; i++)
	{
		tcpoffset[i] = 0.0;
	}
	tcpoffset[TOOL] = 170.0;

	m_OffsetX.SetWindowText("0.000");
	m_OffsetY.SetWindowText("0.000");
	m_OffsetZ.SetWindowText("0.000");
	m_OffsetT.SetWindowText("170.000");

	// Show Offset Value //
	m_OffsetFont = new CFont;
	m_OffsetFont->CreatePointFont(130, "Vimes New Roman");
	m_ShowOffset.SetFont(m_OffsetFont);
	show_offset.Format("%.3f\n\n%.3f\n\n%.3f\n\n%.3f", tcpoffset[0], tcpoffset[1], tcpoffset[2], tcpoffset[3]);
	m_ShowOffset.SetWindowText(show_offset);

	// NC-Editer List //
	m_NCList.GetWindowRect(&rect);
	m_NCList.SetExtendedStyle(LVS_EX_FULLROWSELECT | LVS_EX_HEADERDRAGDROP);

	LV_COLUMN lvc;
	memset(&lvc, 0, sizeof(lvc));

	lvc.mask = LVCF_FMT | LVCF_SUBITEM | LVCF_TEXT | LVCF_WIDTH;
	lvc.fmt = LVCFMT_LEFT;
	lvc.pszText = _T("Line No.");
	lvc.iSubItem = 0;
	lvc.cx = rect.Width() / 5;
	m_NCList.InsertColumn(0, &lvc);

	if (first)
	{
		CButton* TOVInput = (CButton*)GetDlgItem(IDC_RA_TOV_INPUT);
		TOVInput->SetCheck(BST_CHECKED);
	}
}

BOOL CRobControllerDlg::CreateSharedMemory()
{
	HANDLE mSHV = NULL;
	CString InfoStr;

	mSHV = RtCreateSharedMemory((DWORD)PAGE_READWRITE, (DWORD)0, (DWORD) sizeof(SHV), SHM_NAME, (LPVOID*)&shv);

	if (mSHV == NULL)					// Fail to create shared memory
	{
		InfoStr.Format("Fail to create share memory!!!\nError Code = (%d)", GetLastError());
		AfxMessageBox(InfoStr);
		return FALSE;
	}

	return TRUE;
}

void CRobControllerDlg::UnitConversion()
{
	double gear_ratio[6] = { 80.0, 100.0, 80.0, 81.0, 80.0, 50.0 };
	int    pulse[6] = { 262144, 262144, 262144, 262144, 262144, 262144 };

	for (int i = AXIS1; i < TOTAL_AXES; i++)
	{
		shv->UnitConversion.Gear_Ratio[i] = gear_ratio[i];
		shv->UnitConversion.PULSE[i] = pulse[i];
		shv->UnitConversion.Deg2Pulse[i] = shv->UnitConversion.PULSE[i] * 4.0 / 360.0 * shv->UnitConversion.Gear_Ratio[i];
		shv->UnitConversion.Pulse2Deg[i] = 360.0 / shv->UnitConversion.PULSE[i] / 4.0 / shv->UnitConversion.Gear_Ratio[i];
	}
}

void CRobControllerDlg::CommunicationInit()
{
	HANDLE mEVENT;

	////  OPEN EVENT  ////
	mEVENT = RtOpenEvent(NULL, 0, EVN_NAME_START_MASTER);
	if (mEVENT == NULL) { AfxMessageBox("Open Event failed!"); return; }

	////  SET  EVENT  TO  SIGNALED  ////
	RtSetEvent(mEVENT);

	shv->UIStop = 0;
	shv->Velcity = 10;
}

UINT CRobControllerDlg::WriteProc(LPVOID pParam)
{
	CRobControllerDlg* pThis = (CRobControllerDlg *)pParam;
	return pThis->Work();
}

UINT CRobControllerDlg::Work()
{
	OpenGrip = TRUE;

	while (OpenGrip)
	{
		if (shv->GOpen)
		{
			fopen_s(&FileOpen, saveopen, "w");
			fclose(FileOpen);
			shv->GOpen = FALSE;
		}
		else if (shv->GClose)
		{
			fopen_s(&FileClose, saveclose, "w");
			fclose(FileClose);
			shv->GClose = FALSE;
		}
		else if (shv->GMove)
		{
			fopen_s(&FileMove, savemove, "w");
			if (shv->GPosition > 85){ shv->GPosition = 85; }
			else { shv->GPosition = shv->GPosition;}

			fprintf(FileMove, "M%d,S%d,F%d;", shv->GPosition, shv->GSpeed, shv->GForce);
			fclose(FileMove);
			shv->GMove = FALSE;
		}
		Sleep(200);
	}

	return TRUE;
}

UINT CRobControllerDlg::WriteProc1(LPVOID pParam)
{
	CRobControllerDlg* pThis = (CRobControllerDlg *)pParam;
	return pThis->Work1();
}

UINT CRobControllerDlg::Work1()
{
	CString delay_str;
	char* line;
	char  *token, *next_token, NULLString[] = ",\t\n{}";
	startandend = TRUE;
	while (startandend)
	{
		ShowData();
		Sleep(1500);
	}

	if (cont == 1){ SetNCEditor(_T("C:\\Users\\user\\Desktop\\Data\\vision.txt")); }  //Read Data

	if (NCRead() == FALSE){ AfxMessageBox("NCRead Error!!!"); } //Data to NC code

	idx = 0;

	while (idx < widx)
	{
		_strupr_s(nc[idx], 255);
		line = nc[idx];
		token = strtok_s(line, NULLString, &next_token);
		while (token != NULL && *token != ';')
		{
			if (*token == ' ') token = token + 1;
			if (*token == 'J') txtpoint[MODE] = JOINT;
			if (*token == 'P') txtpoint[MODE] = PTP;
			if (*token == 'L') txtpoint[MODE] = CP;
			if (*token == 'G') txtpoint[MODE] = GRIP;
			if (*token == 'O') { txtpoint[MODE] = VAC; SetValue(0, token);}
			if (*token == 'X') SetValue(X, token);
			if (*token == 'Y') SetValue(Y, token);
			if (*token == 'Z') SetValue(Z, token);
			if (*token == 'R')
			{
				token = token + 1;
				if (*token == 'A') SetValue(A, token);
				if (*token == 'B') SetValue(B, token);
				if (*token == 'C') SetValue(C, token);
			}
			if (*token == 'V') SetValue(7, token);
			if (*token == 'M') SetValue(0, token);
			if (*token == 'F') SetValue(1, token);
			if (*token == 'S') SetValue(2, token);
			else { ; }
			token = strtok_s(NULL, NULLString, &next_token);
		}
		if (cnt == TRUE)
		{
			cnt = FALSE;
			if (txtpoint[7] <= 0.001) txtpoint[7] = 1;
			else if (txtpoint[7] >= 100) txtpoint[7] = 100;

			GetDlgItemText(IDC_ED_GDELAY, delay_str);
			shv->GDelay = atof(delay_str) * 1000; // unit: msec

			shv->NCFIFO[shv->NCnum].CtrMode = txtpoint[MODE];
			if (shv->NCFIFO[shv->NCnum].CtrMode == PTP || shv->NCFIFO[shv->NCnum].CtrMode == CP)
			{
				for (int i = X; i <= C; i++)
				{
					shv->NCFIFO[shv->NCnum].Cmd[i] = txtpoint[i];
				}
				shv->NCFIFO[shv->NCnum].Cmd[Z] = shv->NCFIFO[shv->NCnum].Cmd[Z] + tcpoffset[Z];
				shv->NCFIFO[shv->NCnum].RobVel = txtpoint[7];
			}
			else if (shv->NCFIFO[shv->NCnum].CtrMode == JOINT)
			{
				for (int i = AXIS1; i < TOTAL_AXES; i++)
				{
					shv->NCFIFO[shv->NCnum].Cmd[i] = txtpoint[i];
				}
				shv->NCFIFO[shv->NCnum].RobVel = txtpoint[7];
			}
			else if (shv->NCFIFO[shv->NCnum].CtrMode == GRIP)
			{
				for (int i = X; i <= C; i++)
				{
					shv->NCFIFO[shv->NCnum].Cmd[i] = shv->NCFIFO[shv->NCnum-1].Cmd[i];
				}
				for (int i = 0; i < 3; i++)
				{
					shv->NCFIFO[shv->NCnum].Gripara[i] = txtpoint[i]; 
				}
			}
			else if (shv->NCFIFO[shv->NCnum].CtrMode == VAC)
			{
				for (int i = X; i <= C; i++)
				{
					shv->NCFIFO[shv->NCnum].Cmd[i] = shv->NCFIFO[shv->NCnum - 1].Cmd[i];
				}
				shv->NCFIFO[shv->NCnum].Vac = (int)txtpoint[0];
			}
			shv->NCnum = shv->NCnum + 1;
		}
		idx++;
	}
	RemoveTxt();
	return TRUE;
}

void CRobControllerDlg::Forward_Kinematic(double DEG[6], double* TCP, double* TOV)
{
	double C1, C2, C3, C4, C5, C6, S1, S2, S3, S4, S5, S6, C23, S23;
	double RAD[6], UVW[3][3];
	double d6h = d6 + shv->ToolOffset;

	ZeroMemory(&RAD, sizeof(RAD));
	for (int i = AXIS1; i < TOTAL_AXES; i++)	RAD[i] = DEG[i] * DEG2RAD;

	C1 = cos(RAD[AXIS1]), C2 = cos(RAD[AXIS2]), C3 = cos(RAD[AXIS3]);
	C4 = cos(RAD[AXIS4]), C5 = cos(RAD[AXIS5]), C6 = cos(RAD[AXIS6]);
	S1 = sin(RAD[AXIS1]), S2 = sin(RAD[AXIS2]), S3 = sin(RAD[AXIS3]);
	S4 = sin(RAD[AXIS4]), S5 = sin(RAD[AXIS5]), S6 = sin(RAD[AXIS6]);
	C23 = cos(RAD[AXIS2] - RAD[AXIS3]);
	S23 = sin(RAD[AXIS2] - RAD[AXIS3]);

	UVW[0][0] = C1 * S23 * (C4 * C5 * C6 + S4 * S6) - C1 * C23 *S5 * C6 + S1 * (C4 * S6 - S4 * C5 * C6);
	UVW[1][0] = S1 * S23 * (C4 * C5 * C6 + S4 * S6) - S1 * C23 *S5 * C6 - C1 * (C4 * S6 - S4 * C5 * C6);
	UVW[2][0] = C23 * (C4 * C5 * C6 + S4 * S6) + S23 * S5 * C6;
	UVW[0][1] = C1 * S23 * (S4 * C6 - C4 * C5 * S6) + C1 * C23 * S5 * S6 + S1 * (S4 * C5 * S6 + C4 * C6);
	UVW[1][1] = S1 * S23 * (S4 * C6 - C4 * C5 * S6) + S1 * C23 * S5 * S6 - C1 * (S4 * C5 * S6 + C4 * C6);
	UVW[2][1] = C23 * (S4 * C6 - C4 * C5 * S6) - S23 * S5 * S6;
	UVW[0][2] = C1 * S23 * C4 * S5 + C1 * C23 * C5 - S1 * S4 * S5;
	UVW[1][2] = S1 * S23 * C4 * S5 + S1 * C23 * C5 + C1 * S4 * S5;
	UVW[2][2] = C23 * C4 * S5 - S23 * C5;

	TCP[X] = C1 * (a1 + C23 * (d6h * C5 + d4) + a2 * S2 + S23 * (a3 + d6h * C4 * S5)) - d6h * S1 * S4 * S5;
	TCP[Y] = S1 * (a1 + C23 * (d6h * C5 + d4) + a2 * S2 + S23 * (a3 + d6h * C4 * S5)) + d6h * C1 * S4 * S5;
	TCP[Z] = d1 - S23 * (d6h * C5 + d4) + a2 * C2 + C23 * (a3 + d6h * C4 * S5);

	R2Eul(UVW, &TOV[0]);
}

void CRobControllerDlg::R2Eul(double R[3][3], double* EUL)
{
	double RAD[3] = { 0.0, 0.0, 0.0 };
	double U[3], V[3], W[3];

	ZeroMemory(&RAD, sizeof(RAD));

	for (int i = X; i <= Z; i++){
		U[i] = R[i][0];	V[i] = R[i][1];	W[i] = R[i][2];
	}

	RAD[BETA] = atan2(sqrt(pow(W[X], 2) + pow(W[Y], 2)), W[Z]);

	if (fabs(sin(RAD[BETA])) <= ERRC){
		RAD[GAMA] = 0.0;
		RAD[AFA] = atan2(V[X], U[X]);
	}
	else{
		RAD[AFA] = atan2(W[X], (-W[Y]));
		RAD[GAMA] = atan2(U[Z], V[Z]);
	}

	if (fabs(RAD[AFA]) + fabs(RAD[GAMA]) >= PI){
		RAD[BETA] = atan2(-sqrt(pow(W[X], 2) + pow(W[Y], 2)), W[Z]);
		RAD[AFA] = atan2(-W[X], W[Y]);
		RAD[GAMA] = atan2(-U[Z], -V[Z]);
	}

	for (int i = AFA; i < TOTAL_TOV; i++){ EUL[i] = RAD[i] * RAD2DEG; }
}

void CRobControllerDlg::SetTCPOffset(double offset[4])
{
	for (int i = X; i <= Z; i++)
		shv->TCPOffset[i] = offset[i];
	shv->ToolOffset = offset[TOOL];
}

void CRobControllerDlg::SetNCEditor(CString path)
{
	errno_t err;
	CString express;
	char    buf[255];
	UINT    index = 1, count = 0;
	int     width, width_max = 490;
	int     peradd = 0;
	int     percentagecount = 0;
	newfPath = path;

	m_NCList.SetColumnWidth(0, width_max);

	if ((err = fopen_s(&fp, path, "r")) != NULL)
		AfxMessageBox("ERROR");
	//clear all list items //
	m_NCList.DeleteAllItems();
	m_NCList.LockWindowUpdate();

	peradd = (int)((count / 100) + 0.5);
	while (!feof(fp))
	{
		//get line string //
		fgets(buf, sizeof(buf), fp);

		//show NC data information//
		express.Format("%s", buf);
		m_NCList.InsertItem(index, express);
		width = m_NCList.GetStringWidth(express);
		if (width > width_max)
			m_NCList.SetColumnWidth(0, width + 20);
		width_max = max(width, width_max);
		index++;

		if (index >= (UINT)(peradd*percentagecount))
		{
			percentagecount++;
		}
	}

	m_NCList.UnlockWindowUpdate();
	fclose(fp);

	//set the line number of NC file to the start of the program//
	m_NCList.SetSelectionMark(0);
	m_NCList.SetItemState(0, LVIS_SELECTED, LVIS_SELECTED | LVIS_FOCUSED);
	m_NCList.EnsureVisible(0, TRUE);
}

BOOL CRobControllerDlg::NCRead()
{
	errno_t err;
	if ((err = fopen_s(&fp, newfPath, "r")) != NULL)
		return FALSE;
	ZeroMemory(&nc, sizeof(nc));
	ZeroMemory(&shv->NCFIFO, sizeof(shv->NCFIFO));
	ZeroMemory(&shv->CVFFIFO, sizeof(shv->CVFFIFO));
	widx = 0;	
	while (!feof(fp))
	{
		nc[widx] = (char*)malloc(sizeof(char[255]));
		if (fgets(nc[widx], 255, fp) == NULL)
			break;
		widx++;
	}
	fclose(fp);
	return TRUE;
}

BOOL CRobControllerDlg::SetPoint(int axis, char *token)
{
	double val = atof(token + 1);

	if (strlen(token) <= 2)
		return FALSE;

	cnt = TRUE;
	ncpoint[axis] = val;
	
	return TRUE;
}

void CRobControllerDlg::PM2NFU()
{
	CString str;
	int i = 0;
	char* line;
	char  *token, *next_token, NULLString[] = ",\t\n{}";
	shv->NCnum = 0;
	if (NCRead() == FALSE) AfxMessageBox("NCRead Error!!!");
	idx = 0;
	while (idx < widx)
	{
		_strupr_s(nc[idx], 255);
		line = nc[idx];
		token = strtok_s(line, NULLString, &next_token);
		while (token != NULL && *token != ';')
		{
			if (*token == ' ') token = token + 1;
			if (*token == 'P') ncpoint[MODE] = PTP;
			if (*token == 'D') ncpoint[MODE] = CP;
			if (*token == 'G') ncpoint[MODE] = GRIP;
			if (*token == 'X') SetPoint(X, token);
			if (*token == 'Y') SetPoint(Y, token);
			if (*token == 'Z') SetPoint(Z, token);
			if (*token == 'A')
			{
				token = token + 1;
				if (*token == ' ')	SetPoint(A, token);
			}
			if (*token == 'B') SetPoint(B, token);
			if (*token == 'C') SetPoint(C, token);
			if (*token == 'M') SetPoint(0, token);
			if (*token == 'F') SetPoint(1, token);
			if (*token == 'S') SetPoint(2, token);
			else { ; }
			token = strtok_s(NULL, NULLString, &next_token);
		}
		if (cnt == TRUE)
		{
			cnt = FALSE;
			
			for (int i = X; i <= C; i++)
				point[i] = ncpoint[i];

			Rpy2Eul(point, &nfu[0]);

			if (shv->Velcity <= 0.001) shv->Velcity = 1;
			else if (shv->Velcity >= 100) shv->Velcity = 100;

			shv->NCFIFO[shv->NCnum].CtrMode = ncpoint[MODE];

			if (shv->NCFIFO[shv->NCnum].CtrMode == PTP || shv->NCFIFO[shv->NCnum].CtrMode == CP)
			{
				for (int i = X; i <= C; i++)
				{
					shv->NCFIFO[shv->NCnum].Cmd[i] = nfu[i];
				}
			}
			else if (shv->NCFIFO[shv->NCnum].CtrMode == GRIP)
			{
				for (int i = 0; i < 6; i++)
				{
					shv->NCFIFO[shv->NCnum].Cmd[i] = shv->NCFIFO[shv->NCnum - 1].Cmd[i];
				}
				for (int i = 0; i < 3; i++)
				{
					shv->NCFIFO[shv->NCnum].Gripara[i] = ncpoint[i];
				}
			}
			shv->NCnum = shv->NCnum + 1;
		}
		idx++;
	}

	//fopen_s(&fp, "C:\\Users\\User\\Desktop\\New.txt", "w");
	//for (int j = 0; j <shv->NCnum; j++)
	//{
	//	for (int i = X; i <= C; i++)
	//	{
	//		fprintf(fp, "%f\t", shv->data[j].Cmd[i]);
	//	}
	//	fprintf(fp, "\n");
	//}
	//fclose(fp);
	//MessageBox("OK");
}

void CRobControllerDlg::Rpy2Eul(double NC[6], double *NCnfu)
{
	double RAD[3], U[3], V[3], W[3];
	double Cr, Cp, Cy, Sr, Sp, Sy;

	ZeroMemory(&RAD, sizeof(RAD));
	for (int i = AFA; i <= GAMA; i++){
		RAD[i] = NC[i + TOTAL_TCP] * DEG2RAD;
	}

	Cr = cos(RAD[ROLL]), Cp = cos(RAD[PITCH]), Cy = cos(RAD[YAW]);
	Sr = sin(RAD[ROLL]), Sp = sin(RAD[PITCH]), Sy = sin(RAD[YAW]);

	U[X] = Cp * Sy;
	U[Y] = -Cp * Cy;
	U[Z] = -Sp;
	V[X] = -Sr * Sp * Sy - Cr * Cy;
	V[Y] = Sr * Sp * Cy - Cr * Sy;
	V[Z] = -Sr * Cp;
	W[X] = -Cr * Sp * Sy + Sr * Cy;
	W[Y] = Cr * Sp * Cy + Sr * Sy;
	W[Z] = -Cr * Cp;

	RAD[BETA] = atan2(sqrt(pow(W[X], 2) + pow(W[Y], 2)), W[Z]);

	if (fabs(sin(RAD[BETA])) <= ERRC){
		RAD[GAMA] = 0.0;
		RAD[AFA] = atan2(V[X], U[X]);
	}
	else{
		RAD[AFA] = atan2(W[X], (-W[Y]));
		RAD[GAMA] = atan2(U[Z], V[Z]);
	}

	if (fabs(RAD[AFA]) + fabs(RAD[GAMA]) >= PI){
		RAD[BETA] = atan2(-sqrt(pow(W[X], 2) + pow(W[Y], 2)), W[Z]);
		RAD[AFA] = atan2(-W[X], W[Y]);
		RAD[GAMA] = atan2(-U[Z], -V[Z]);
	}

	for (int i = AFA; i <= GAMA; i++) { NCnfu[i + TOTAL_TCP] = RAD[i] * RAD2DEG; }

	NCnfu[X] = tcpoffset[X] + NC[Y];
	NCnfu[Y] = tcpoffset[Y] - NC[X];
	NCnfu[Z] = tcpoffset[Z] + NC[Z] + d1;
}

void CRobControllerDlg::ChoosenTOV()
{
	CString strText;
	CButton* TOVInput = (CButton*)GetDlgItem(IDC_RA_TOV_INPUT);
	CButton* TOVForward = (CButton*)GetDlgItem(IDC_RA_TOV_FORWARD);
	CButton* TOVDown = (CButton*)GetDlgItem(IDC_RA_TOV_DOWN);

	if (TOVInput->GetCheck() == BST_CHECKED)
	{
		GetDlgItem(IDC_ED_TOVA)->EnableWindow(true);
		GetDlgItem(IDC_ED_TOVB)->EnableWindow(true);
		GetDlgItem(IDC_ED_TOVC)->EnableWindow(true);
	}

	if (TOVForward->GetCheck() == BST_CHECKED)
	{
		GetDlgItem(IDC_ED_TOVA)->EnableWindow(false);
		GetDlgItem(IDC_ED_TOVB)->EnableWindow(false);
		GetDlgItem(IDC_ED_TOVC)->EnableWindow(false);

		SetDlgItemText(IDC_ED_TOVA, "90.0");
		SetDlgItemText(IDC_ED_TOVB, "90.0");
		SetDlgItemText(IDC_ED_TOVC, "90.0");
	}

	if (TOVDown->GetCheck() == BST_CHECKED)
	{
		GetDlgItem(IDC_ED_TOVA)->EnableWindow(false);
		GetDlgItem(IDC_ED_TOVB)->EnableWindow(false);
		GetDlgItem(IDC_ED_TOVC)->EnableWindow(false);

		SetDlgItemText(IDC_ED_TOVA, "0.0");
		SetDlgItemText(IDC_ED_TOVB, "180.0");
		SetDlgItemText(IDC_ED_TOVC, "0.0");
	}
}

void CRobControllerDlg::BLKgeometrics(){
	int mas;
	double dsmax, si;
	idx = 1;
	for (int i = 0; i < 6; i++){ shv->NCFIFO[0].ds[i] = 0.0; }

	while (idx < shv->NCnum){ //NCnum
		pidx = idx - 1;
		for (int i = 0; i < 6; i++){
			shv->NCFIFO[idx].ds[i] = shv->NCFIFO[idx].Cmd[i] - shv->NCFIFO[pidx].Cmd[i];
			//if (abs(shv->NCFIFO[idx].ds[i]) < Res[i]){ shv->NCFIFO[idx].ds[i] = 0.0; }
		}
		shv->NCFIFO[pidx].len = Norm3(shv->NCFIFO[idx].ds[0], shv->NCFIFO[idx].ds[1], shv->NCFIFO[idx].ds[2]);

		if (shv->NCFIFO[pidx].len != 0.0)
			for (int i = 0; i<3; i++){ shv->NCFIFO[pidx].T[i] = shv->NCFIFO[idx].ds[i] / shv->NCFIFO[pidx].len; }
		else
			for (int i = 0; i<3; i++){ shv->NCFIFO[pidx].T[i] = 0; }

		for (int i = 3; i<6; i++){
			if (shv->NCFIFO[idx].ds[i] > 0.0)		{ shv->NCFIFO[pidx].T[i] = 1.0; }
			else if (shv->NCFIFO[idx].ds[i] < 0.0)	{ shv->NCFIFO[pidx].T[i] = -1.0; }
			else									{ shv->NCFIFO[pidx].T[i] = 0.0; }
		}
		idx = idx + 1;
	}
	for (int i = 0; i < 6; i++){ shv->NCFIFO[shv->NCnum - 1].T[i] = 0; }
	shv->NCFIFO[shv->NCnum - 1].len = 0;

	int bpcnt = 0, bpv, Nbp;
	idx = 1;
	while (idx < shv->NCnum){
		bpv = 0;	pidx = idx - 1;
		for (int i = 0; i < 6; i++){
			if ((shv->NCFIFO[pidx].T[i] != 0 && shv->NCFIFO[idx].T[i] == 0) || (shv->NCFIFO[pidx].T[i] == 0 && shv->NCFIFO[idx].T[i] != 0))
				shv->NCFIFO[idx].fbp[i] = 1;
			else if (shv->NCFIFO[pidx].T[i] * shv->NCFIFO[idx].T[i] < 0.0)
				shv->NCFIFO[idx].fbp[i] = 2;
			else
				shv->NCFIFO[idx].fbp[i] = 0;
			bpv = bpv + shv->NCFIFO[idx].fbp[i];
		}
		if (bpv != 0){ shv->NCFIFO[idx].bpv = bpv;	bpcnt = bpcnt + 1; shv->NCFIFO[bpcnt].bkp = idx; }
		else		 { shv->NCFIFO[idx].bpv = 0; }
		idx = idx + 1;
	}
	Nbp = bpcnt;

	BLKgeoFittingt();

	idx = 1;
	for (int i = 0; i < 6; i++){ shv->CVFFIFO[0].ds[i] = 0.0; }

	while (idx <= shv->CVFnum){
		pidx = idx - 1;
		for (int i = 0; i < 6; i++)
			shv->CVFFIFO[idx].ds[i] = shv->CVFFIFO[idx].Cmd[i] - shv->CVFFIFO[pidx].Cmd[i];
		shv->CVFFIFO[pidx].len = Norm3(shv->CVFFIFO[idx].ds[0], shv->CVFFIFO[idx].ds[1], shv->CVFFIFO[idx].ds[2]);

		dsmax = abs(shv->CVFFIFO[idx].ds[0]); mas = 0;
		for (int i = 1; i<6; i++){
			if (abs(shv->CVFFIFO[idx].ds[i]) >= dsmax){ dsmax = abs(shv->CVFFIFO[idx].ds[i]); mas = i; }
		}
		if (dsmax == 0.0){ printf("error"); }
		shv->CVFFIFO[idx].dsmax = dsmax; shv->CVFFIFO[idx].mas = mas;
		if (shv->CVFFIFO[idx].ds[mas] >= 0.0)	{ si = 1.0; }
		else									{ si = -1.0; }
		for (int i = 0; i < 6; i++){ shv->CVFFIFO[idx].Kma[i] = si*shv->CVFFIFO[idx].ds[i] / shv->CVFFIFO[idx].ds[mas]; }
		shv->CVFFIFO[idx].Kmt = shv->CVFFIFO[pidx].len / dsmax;

		if (shv->CVFFIFO[pidx].len != 0.0){
			shv->CVFFIFO[idx].Ktm = 1.0 / shv->CVFFIFO[idx].Kmt;
			for (int i = 0; i < 3; i++){ shv->CVFFIFO[pidx].T[i] = shv->CVFFIFO[idx].ds[i] / shv->CVFFIFO[pidx].len; }
		}
		else{
			shv->CVFFIFO[idx].Ktm = 1.0;
			for (int i = 0; i < 3; i++){ shv->CVFFIFO[pidx].T[i] = 0; }
		}

		for (int i = 3; i<6; i++){
			if (shv->CVFFIFO[idx].ds[i] > 0.0)		{ shv->CVFFIFO[pidx].T[i] = 1.0; }
			else if (shv->CVFFIFO[idx].ds[i] < 0.0)	{ shv->CVFFIFO[pidx].T[i] = -1.0; }
			else									{ shv->CVFFIFO[pidx].T[i] = 0.0; }
		}
		for (int i = 0; i < 6; i++){ shv->CVFFIFO[idx].Kta[i] = shv->CVFFIFO[idx].Ktm*shv->CVFFIFO[idx].Kma[i]; }
		idx = idx + 1;
	}
	for (int i = 0; i < 6; i++){ shv->CVFFIFO[shv->CVFnum].T[i] = 0; }
	shv->CVFFIFO[shv->CVFnum].len = 0;
}

void CRobControllerDlg::BLKgeoFittingt(){

	double dP20[3], dP20p2, dP10[3], dP10p2, dP10P20;
	double u, Lp;
	int bcnt, chkidx;
	int ncidx, nlidx;
	int loop;

	for (int j = 0; j < 6; j++){ shv->CVFFIFO[0].Cmd[j] = shv->NCFIFO[0].Cmd[j]; }
	shv->CVFFIFO[0].Feedrate = shv->NCFIFO[0].Feedrate;
	for (int j = 0; j < 3; j++){ shv->CVFFIFO[0].Gripara[j] = shv->NCFIFO[0].Gripara[j]; }
	shv->CVFFIFO[0].CtrMode = shv->NCFIFO[0].CtrMode;

	idx = 0; ncidx = 0;

	while (ncidx < shv->NCnum - 3){
		bcnt = 1;	nlidx = ncidx + 1;

		if (shv->NCFIFO[nlidx].bpv == 0 && shv->NCFIFO[nlidx].CtrMode != GRIP ){
			loop = 1;
			while (loop){
				for (int i = 0; i < 3; i++){ dP20[i] = shv->NCFIFO[nlidx + bcnt].Cmd[i] - shv->NCFIFO[ncidx].Cmd[i]; }
				dP20p2 = VecDot(dP20, dP20, 3);

				for (int i = 0; i < bcnt; i++){
					for (int j = 0; j < 3; j++){ dP10[j] = shv->NCFIFO[ncidx + i].Cmd[j] - shv->NCFIFO[ncidx].Cmd[j]; }
					dP10p2 = VecDot(dP10, dP10, 3);
					dP10P20 = VecDot(dP10, dP20, 3);
					u = dP10P20 / dP20p2;
					if (u <= 1.0 && u >= 0.0){
						Lp = sqrt(abs(dP10p2*dP20p2 - pow(dP10P20, 2)) / dP20p2);
						if (Lp > 1e-3){ loop = 0; break; }
					}
				}//for (int i = 0;i < bcnt;i++)

				if (loop){
					chkidx = nlidx + bcnt; bcnt = bcnt + 1;
					if (chkidx < shv->NCnum - 1){
						if (shv->NCFIFO[chkidx].bpv != 0){ break; }
						if (shv->NCFIFO[chkidx + 1].CtrMode == GRIP){ break; }
					}
					else if (chkidx == shv->NCnum - 1){
						break;
					}
				}//if(loop)
			}//while(loop)
		}

		if (chkidx < shv->NCnum - 1){
			ncidx = ncidx + bcnt; idx = idx + 1;
			for (int j = 0; j < 6; j++){ shv->CVFFIFO[idx].Cmd[j] = shv->NCFIFO[ncidx].Cmd[j]; }
			shv->CVFFIFO[idx].Feedrate = shv->NCFIFO[ncidx].Feedrate;
			shv->CVFFIFO[idx].bkp = shv->NCFIFO[ncidx].bkp;	shv->CVFFIFO[idx].bpv = shv->NCFIFO[ncidx].bpv;

			shv->CVFFIFO[idx].CtrMode = shv->NCFIFO[ncidx].CtrMode;
			for (int j = 0; j < 3; j++){ shv->CVFFIFO[idx].Gripara[j] = shv->NCFIFO[ncidx].Gripara[j]; }
		}
	}
	while (ncidx < shv->NCnum-1 || shv->NCFIFO[ncidx + 1].CtrMode == GRIP){
		idx = idx + 1; ncidx = ncidx + 1;
		for (int j = 0; j < 6; j++){ shv->CVFFIFO[idx].Cmd[j] = shv->NCFIFO[ncidx].Cmd[j]; }//shv->NCnum - 1
		shv->CVFFIFO[idx].Feedrate = shv->NCFIFO[ncidx].Feedrate;
		shv->CVFFIFO[idx].bkp = shv->NCFIFO[ncidx].bkp;	shv->CVFFIFO[idx].bpv = shv->NCFIFO[ncidx].bpv;
		shv->CVFFIFO[idx].CtrMode = shv->NCFIFO[ncidx].CtrMode;
		for (int j = 0; j < 3; j++){ shv->CVFFIFO[idx].Gripara[j] = shv->NCFIFO[ncidx].Gripara[j]; }
		shv->CVFnum = idx;
	}
}

double CRobControllerDlg::Norm3(double x, double y, double z)
{
	return sqrt(x*x + y*y + z*z);
}

double CRobControllerDlg::Norm2(double x, double y)
{
	return sqrt(x*x + y*y);
}

double CRobControllerDlg::VecDot(double *a, double *b, int dim)
{
	double sum = 0.0;

	for (int i = 0; i<dim; i++)
		sum = sum + a[i] * b[i];

	return sum;
}

void CRobControllerDlg::ShowData()
{
	cont = 0;

	m_TxtList.ResetContent();

	BOOL bWorking = finder.FindFile(_T("C:\\Users\\user\\Desktop\\Data\\*.*"));
	while (bWorking)
	{
		bWorking = finder.FindNextFile();
		m_TxtList.InsertString(x, finder.GetFileName());
		if (finder.GetFileName() == "vision.txt")
		{
			cont = 1;
			startandend = FALSE;
		}
		x++;
	}
}

BOOL CRobControllerDlg::SetValue(int pos, char *token)
{
	double val = atof(token + 1);

	if (strlen(token) <= 2)
		return FALSE;

	cnt = TRUE;
	txtpoint[pos] = val;

	return TRUE;
}

void CRobControllerDlg::RemoveTxt()
{
	CFile file;
	file.Remove("C:\\Users\\user\\Desktop\\Data\\vision.txt");
	shv->UIReadTxt = 1;
}
