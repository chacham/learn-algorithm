import scala.collection.mutable._

object Solution {
  val Push = """push (\d+)""".r
  val Pop = """pop""".r
  val Size = """size""".r
  val Empty = """empty""".r
  val Top = """top""".r

  def readOps(N: Int) = {
    val inputs = ListBuffer[String]()
    for (i <- 1 to N) {
      inputs += io.StdIn.readLine
    }
    inputs
  }

  def run(ops: List[String], stack: List[Int]): Unit = {
    ops match {
      case hd::tl => {
        hd match {
          case Push(s) => run(tl, s.toInt :: stack)
          case Pop() => stack match {
            case shd::stl => {
              println(shd)
              run(tl, stl)
            }
            case Nil => {
              println(-1)
              run(tl, Nil)
            }
          }
          case Size() => {
            println(stack.length) // List의 length가 traverse하니까 바꿔야함. 파라미터로 stack 크기를 하나 가져오는게 좋을듯
            run(tl, stack)
          }
          case Empty() => {
            println(if (stack.isEmpty) 1 else 0)
            run(tl, stack)
          }
          case Top() => stack match {
            case shd::stl => {
              println(shd)
              run(tl, stack)
            }
            case Nil => {
              println(-1)
              run(tl, stack)
            }
          }
        }
      }
      case Nil => ()
    }
  }

  def main(args: Array[String]): Unit = {
    val N = io.StdIn.readInt
    val OPs = readOps(N).toList
    run(OPs, Nil)
  }
}
