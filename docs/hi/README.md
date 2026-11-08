# BhashaSetu — हिंदी में परिचय

BhashaSetu छोटे और स्वयंसेवी open-source प्रोजेक्ट्स के maintainers की मदद करने वाला **privacy-first, Hindi-first** command-line tool है।

यह tool:

- GitHub issue का छोटा सार और संभावित labels तैयार करता है;
- नए contributors के लिए code या issue को आसान हिंदी में समझाता है;
- Markdown documentation का अनुवाद करता है, जबकि commands, links और code blocks को सुरक्षित रखता है;
- model को भेजने से पहले कुछ सामान्य secrets को redact करता है;
- हर उत्तर को draft रखता है—अपने-आप issue बंद या comment publish नहीं करता।

## जल्दी शुरू करें

```bash
python -m pip install -e ".[openai,dev]"
bhashasetu triage --file examples/issue.json --dry-run
```

`--dry-run` किसी API को call नहीं करता। वास्तविक request के लिए `OPENAI_API_KEY` environment variable सेट करें और output को human reviewer जाँचें।

यह स्वतंत्र community project है और OpenAI से संबद्ध या endorsed नहीं है। पूरी जानकारी के लिए root में [`README.md`](../../README.md) देखें।
