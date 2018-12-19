import com.intellij.openapi.components.ProjectComponent
import com.intellij.openapi.project.Project

import scala.sys.process.Process

class ProjectLoading extends ProjectComponent{
  private var project: Project = _

  /**
    * @param project The current project, i.e. the project which was just opened.
    */
  def this(project: Project, applicationComponent: Nothing) {
    this()
    this.project = project
  }

  override def projectOpened(): Unit = {
    val output = Process("git pull -C " + project.getBasePath).run()
    //Messages.showInfoMessage(output, "GIT")

  }
}
