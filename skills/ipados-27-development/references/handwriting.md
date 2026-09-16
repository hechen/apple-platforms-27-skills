# PencilKit 27 handwriting

Apple documents on-device recognition with `PKStrokeRecognizer`, supporting text extraction, search in strokes, and indexable text. See [Recognizing handwriting and converting it to text](https://developer.apple.com/documentation/pencilkit/recognizing-handwriting-and-converting-to-text) and [PencilKit updates](https://developer.apple.com/documentation/updates/pencilkit).

Keep one recognizer associated with each open drawing. Configure expected languages and avoid confusing canvas zoom with the scale of the stored drawing. Preserve the original `PKDrawing`; recognized text is derived data. If persisting recognition results, record `PKStrokeRecognizer.recognitionVersion` and support refreshing the cache when recognition changes.

Stroke identity and selection APIs can connect selected ink to document operations. Keep undo history and selection stable when recognition finishes asynchronously; discard results for drawings or selections that have since changed. Index only content the user expects to be discoverable, and update/delete indexed text when the drawing changes or disappears.

Validation: mixed-language handwriting, blank strokes, partial selection, undo/redo after conversion, rapid edits while recognition runs, save/reopen, and older-reader behavior. Apple's [handwriting sample](https://developer.apple.com/documentation/pencilkit/building-a-handwriting-recognition-experience-with-pencilkit) requires a physical device with Apple Pencil. Simulator validation does not replace that check.
