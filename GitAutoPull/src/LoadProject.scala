import com.intellij.openapi.components.ApplicationComponent
import com.intellij.openapi.project.Project

class LoadProject extends ApplicationComponent {
  override def getComponentName: String = {
    "GitAutoPull"
  }

  override def initComponent(): Unit = {
    import com.intellij.ide.DataManager
    import com.intellij.openapi.actionSystem.DataConstants
    val dataContext = DataManager.getInstance.getDataContext
    val project: Project = dataContext.getData(DataConstants.PROJECT).asInstanceOf[Project]
    import sys.process._
    "git pull -C " + project.getBasePath !
  }

  override def disposeComponent(): Unit = {}
}
