///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version 3.10.1-0-g8feb16b3)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#pragma once

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/filepicker.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/combobox.h>
#include <wx/button.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/sizer.h>
#include <wx/textctrl.h>
#include <wx/gauge.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class MyFrame
///////////////////////////////////////////////////////////////////////////////
class MyFrame : public wxFrame
{
	private:

	protected:
		wxFilePickerCtrl* m_filePicker;
		wxComboBox* m_comboBox;
		wxButton* m_button1;
		wxButton* m_button2;
		wxButton* m_button3;
		wxTextCtrl* m_textCtrl;
		wxGauge* m_gauge;

		// Virtual event handlers, override them in your derived class
		virtual void CalculateHash( wxCommandEvent& event ) { event.Skip(); }
		virtual void Clear( wxCommandEvent& event ) { event.Skip(); }
		virtual void Quit( wxCommandEvent& event ) { event.Skip(); }


	public:

		MyFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxEmptyString, const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,500 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );

		~MyFrame();

};

