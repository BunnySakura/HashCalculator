#include "show_my_frame.h"
#include "hash_algorithms.h"
#include <wx/clipbrd.h>

#include <stdio.h>
#include <vector>
#include <string>
#include <fstream>
#include <filesystem>

#define BUFFER_SIZE 65536

ShowMyFrame::ShowMyFrame(wxWindow* parent)
    : MyFrame(parent)
{
}

void ShowMyFrame::CalculateHash(wxCommandEvent& event)
{
    std::string file_path = m_filePicker->GetFileName().GetFullPath(); // 文件绝对路径。

    // 检测是否已选择文件，未选择则不执行。
    if (file_path == "")
    {
        m_textCtrl->WriteText("请选择文件！\n");
    }
    else
    {
        // 根据选择的算法实例化对应子类，默认SHA-512。
        HashAlgorithms* hash_algorithm;
        if (m_comboBox->GetStringSelection() == "SHA-512")
        {
            hash_algorithm = new SHA512_Hash;
        }
        else if (m_comboBox->GetStringSelection() == "SHA-256")
        {
            hash_algorithm = new SHA256_Hash;
        }
        else if (m_comboBox->GetStringSelection() == "MD5")
        {
            hash_algorithm = new MD5_Hash;
        }
        else
        {
            hash_algorithm = new MD5_Hash;
        }

        // 二进制打开文件。
        std::ifstream file_read(file_path, std::ios::binary);

        // 摘要计算，并更新进度条。
        char* buffer = new char[BUFFER_SIZE];
        std::filesystem::path get_file_size(file_path);                 // 调用filesystem库获取文件大小。
        m_gauge->SetRange(std::filesystem::file_size(get_file_size));   // 进度条范围设为文件大小。
        uintmax_t calculated_file_size = 0;                             // 已计算摘要的大小。
        while (!file_read.eof())
        {
            file_read.read(buffer, BUFFER_SIZE);
            hash_algorithm->update(buffer, file_read.gcount());
            calculated_file_size += file_read.gcount();
            m_gauge->SetValue(calculated_file_size); // 更新进度条。
        }
        delete[] buffer;

        // 摘要结果处理为16进制字符串准备输出。
        std::string result_str;
        std::vector<uint8_t> result(hash_algorithm->GetResult());
        for (uint8_t& hex : result)
        {
            char hex_str[3] = { 0 }; // snprintf会自动添加'\0'
            snprintf(hex_str, 3, "%02x", hex);
            result_str.append(hex_str);
        }

        // 将一些文本写入剪贴板，并输出到文本框。
        if (wxTheClipboard->Open())
        {
            // 此数据对象由剪贴板保存，
            // 所以不要在应用程序中删除它们。
            wxTheClipboard->SetData(new wxTextDataObject(result_str));
            wxTheClipboard->Close();
        }
        m_textCtrl->WriteText(file_path + "的摘要为（已复制到剪贴板）：\n" + result_str + "\n\n");

        delete hash_algorithm;
    }
}

void ShowMyFrame::Clear(wxCommandEvent& event)
{
    m_textCtrl->Clear();
}

void ShowMyFrame::Quit(wxCommandEvent& event)
{
    Destroy();
}
