
(defconstant +size+ 10)

(defun create-checkerboard ()
    (let ((board (make-array '(10 10))))
        (setf (aref board 0 0) 52570)
    board)
)

(defparameter *checkerboard* (create-checkerboard))
(print *checkerboard*)
(terpri)(quit)
