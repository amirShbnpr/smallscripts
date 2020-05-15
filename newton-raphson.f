      program root
        double precision x, f, df
        external f, df
        integer date_time(8)
        character (len=12) real_clock(3)
        call date_and_time (real_clock(1),real_clock(2)
     1  , real_clock(3), date_time)
        print *, real_clock(1), real_clock(2), 
     1  real_clock(3) , date_time
        x = 1.0d0 / sqrt(3.0d0)
        call newTon(x, f, df)
        print *, "root is at x = ", x
        call date_and_time (real_clock(1),real_clock(2)
     1  , real_clock(3), date_time)
        print *, real_clock(1), real_clock(2), 
     1  real_clock(3) , date_time
      end
*
*       main function
*

      double precision function f(x)
        double precision x
        f = x**2 + 1
      end
*
*       derivation
*
       double precision function df(x)
        double precision x
        df = 2 * x
       end
*
*       root subroutine
*
        subroutine newTon(x, f, df)
            double precision x, f, df
            double precision error, tol, delta
            parameter (tol = 0.5d-04)
            integer :: i
            i = 1
100         delta = - f(x) / df(x)
            x = x + delta
            i = i + 1
            error = abs(delta / x)
            if (error.gt.tol.and.i.le.30) then
                goto 100
            else
                print *, "No limited amount of roots"
            end if
        end
