Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
... Write a pyhton to display the following:
... 
...  Welcome to python program
...  
... """
... 
'\nWrite a pyhton to display the following:\n\n Welcome to python program\n \n'
>>> w = """ 
...     *   * *** *   *** *** **  ** ***
...     * * * **  *   *   * * * ** * **
...     ** ** *** *** *** *** *    * ***
...     """
... 
>>> t = """
...                 *** ***
...                  *  * *
...                  *  ***
...     """
... 
>>> p = """
...         *** * * *** * * *** ** *          
...         * * * *  *  *** * * ** *
...         *** ***  *  * * * * * **
...         *    *   *  * * *** *  *
...     """
>>> py = """
...     *** ***  *** **** ***   *  **  **
...     * * * *  * * *    * *   *  **  **
...     *** ***  * * * ** ***  *** * ** *
...     *   *  * *** **** *  * * * *    *
...      """
... 
>>> concat = w + " " + t + " " + p + " " + py;
>>> print(concat);
 
    *   * *** *   *** *** **  ** ***
    * * * **  *   *   * * * ** * **
    ** ** *** *** *** *** *    * ***
     
                *** ***
                 *  * *
                 *  ***
     
        *** * * *** * * *** ** *          
        * * * *  *  *** * * ** *
        *** ***  *  * * * * * **
        *    *   *  * * *** *  *
     
    *** ***  *** **** ***   *  **  **
    * * * *  * * *    * *   *  **  **
    *** ***  * * * ** ***  *** * ** *
    *   *  * *** **** *  * * * *    *
     
