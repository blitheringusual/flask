Option Explicit

' Get command-line arguments
Dim strInputFile, strOutputFile
strInputFile = WScript.Arguments(0)
strOutputFile = WScript.Arguments(1)

' Check if arguments are provided
If strInputFile = "" Or strOutputFile = "" Then
    MsgBox "Usage: cleaner.vbs --input_file --output_file"
    WScript.Quit
End If

' Check if the input file exists
Dim objFSO, objInputFile, objOutputFile
Set objFSO = CreateObject("Scripting.FileSystemObject")
If Not objFSO.FileExists(strInputFile) Then
    MsgBox "Error: The specified input file does not exist."
    WScript.Quit
End If

' Open the input file for reading
Set objInputFile = objFSO.OpenTextFile(strInputFile, 1) ' ForReading

' Open the output file for writing
Set objOutputFile = objFSO.CreateTextFile(strOutputFile, True) ' Create or overwrite

' Process each line of the file
Do While Not objInputFile.AtEndOfStream
    ' Read a line from the file
    Dim strLine
    strLine = objInputFile.ReadLine

    ' Find the position of the first semicolon
    Dim intFirstSemicolonPos
    intFirstSemicolonPos = InStr(strLine, ";")

    ' Process the line based on the semicolon's presence
    Dim strOutput
    If intFirstSemicolonPos > 0 Then
        ' Separate the first part and the rest
        Dim firstPart, restPart
        firstPart = Left(strLine, intFirstSemicolonPos - 1)
        restPart = Mid(strLine, intFirstSemicolonPos + 1)
        
        ' Replace the remaining semicolons with spaces
        restPart = Replace(restPart, ";", " ")
        
        ' Combine the results
        strOutput = firstPart & "; " & restPart
    Else
        ' If no semicolon is found, just output the original content
        strOutput = strLine
    End If

    ' Write the modified line to the output file
    objOutputFile.WriteLine strOutput
Loop

' Close the files
objInputFile.Close
objOutputFile.Close

' Display a message when done
MsgBox "Cleaning complete!"
