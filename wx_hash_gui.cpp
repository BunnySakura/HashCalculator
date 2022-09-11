///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "wx_hash_gui.h"

///////////////////////////////////////////////////////////////////////////

MyFrame::MyFrame( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxSize( 300,300 ), wxDefaultSize );
	this->SetBackgroundColour( wxSystemSettings::GetColour( wxSYS_COLOUR_WINDOW ) );

	wxBoxSizer* mainBoxSizer;
	mainBoxSizer = new wxBoxSizer( wxVERTICAL );

	m_filePicker = new wxFilePickerCtrl( this, wxID_ANY, wxEmptyString, wxT("Select a file"), wxT("*.*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE|wxFLP_FILE_MUST_EXIST );
	mainBoxSizer->Add( m_filePicker, 0, wxALL|wxEXPAND, 0 );

	m_comboBox = new wxComboBox( this, wxID_ANY, wxT("SHA-512"), wxDefaultPosition, wxDefaultSize, 0, NULL, wxCB_READONLY );
	m_comboBox->Append( wxT("SHA-512") );
	m_comboBox->Append( wxT("SHA-256") );
	m_comboBox->Append( wxT("MD5") );
	m_comboBox->SetSelection( 0 );
	mainBoxSizer->Add( m_comboBox, 0, wxALL|wxEXPAND, 0 );

	wxBoxSizer* subBoxSizer;
	subBoxSizer = new wxBoxSizer( wxHORIZONTAL );

	m_button1 = new wxButton( this, wxID_ANY, wxT("计算"), wxDefaultPosition, wxDefaultSize, 0 );
	subBoxSizer->Add( m_button1, 0, wxALL, 0 );


	subBoxSizer->Add( 0, 0, 1, wxEXPAND, 0 );

	m_button2 = new wxButton( this, wxID_ANY, wxT("清屏"), wxDefaultPosition, wxDefaultSize, 0 );
	subBoxSizer->Add( m_button2, 0, wxALL, 0 );


	subBoxSizer->Add( 0, 0, 1, wxEXPAND, 0 );

	m_button3 = new wxButton( this, wxID_ANY, wxT("退出"), wxDefaultPosition, wxDefaultSize, 0 );
	subBoxSizer->Add( m_button3, 0, wxALL, 0 );


	mainBoxSizer->Add( subBoxSizer, 0, wxEXPAND, 0 );

	m_textCtrl = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, wxTE_MULTILINE|wxTE_READONLY );
	mainBoxSizer->Add( m_textCtrl, 1, wxALL|wxEXPAND, 0 );

	m_gauge = new wxGauge( this, wxID_ANY, 100, wxDefaultPosition, wxDefaultSize, wxGA_HORIZONTAL );
	m_gauge->SetValue( 0 );
	mainBoxSizer->Add( m_gauge, 0, wxALL|wxEXPAND, 0 );


	this->SetSizer( mainBoxSizer );
	this->Layout();

	this->Centre( wxBOTH );

	// Connect Events
	m_button1->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame::CalculateHash ), NULL, this );
	m_button2->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame::Clear ), NULL, this );
	m_button3->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame::Quit ), NULL, this );
}

MyFrame::~MyFrame()
{
	// Disconnect Events
	m_button1->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame::CalculateHash ), NULL, this );
	m_button2->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame::Clear ), NULL, this );
	m_button3->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( MyFrame::Quit ), NULL, this );

}
