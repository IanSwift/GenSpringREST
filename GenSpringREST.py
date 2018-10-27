import os
import platform
slash = '\\' if platform.system() == 'Windows' else '/'


def createRootDirectory(directory, resourceName):
    if not os.path.exists(directory + resourceName.lower()+'s'):
        os.makedirs(directory + resourceName.lower()+'s')
    return directory + resourceName.lower()+'s'

def createControllerClass(directory, packagePrefix, resourceName, idClass, newline, customPackage):
    file = open(directory + resourceName.capitalize()+'Controller.java', 'w+')
    resources = resourceName.lower() + 's'
    resourceClass = resourceName.capitalize()
    resourceInstance = resourceName[0:1].lower() + resourceName[1:]
    controllerClass = resourceName.capitalize()+'Controller'
    serviceClass = resourceName.capitalize() + 'Service'
    serviceInstance = resourceName[0:1].lower() + resourceName[1:] + 'Service'
    file.writelines(
    'package ' + packagePrefix.lower() + '.' + resources + ';' + newline +
    newline +
    (('import ' + customPackage + '.' + idClass + newline + newline) if customPackage else ('')) +
    'import org.springframework.http.HttpStatus;' + newline +
    'import org.springframework.validation.annotation.Validated;' + newline +
    'import org.springframework.web.bind.annotation.ExceptionHandler;' + newline +
    'import org.springframework.web.bind.annotation.RequestMapping;' + newline +
    'import org.springframework.web.bind.annotation.ResponseStatus;' + newline +
    'import org.springframework.web.bind.annotation.RestController;' + newline +
    'import org.springframework.web.bind.annotation.RequestMethod;' + newline +
    'import org.springframework.web.bind.annotation.RequestBody;' + newline +
    'import org.springframework.web.bind.annotation.PathVariable;' + newline +
    newline +
    'import javax.servlet.http.HttpServletRequest;' + newline +
    'import java.time.ZoneOffset;' + newline +
    'import java.time.format.DateTimeFormatter;' + newline +
    'import java.util.List;' + newline +
    'import java.util.Map;' + newline +
    'import java.util.LinkedHashMap;' + newline +
    'import java.util.Date;' + newline +
    newline +
    '@RestController' + newline +
    '@RequestMapping("/' + resources + '")' + newline +
    'public class ' + controllerClass + ' {' + newline +
    newline +
    '    private ' + serviceClass + ' ' + serviceInstance + ';' + newline + 
    newline +
    '    public ' + controllerClass + '('  + serviceClass + ' ' + serviceInstance + ') { ' + newline +
    '        this.' + serviceInstance + ' = ' + serviceInstance + ';' + newline +
    '    }' + newline +
    newline +
    '    @RequestMapping("")' + newline +
    '    @ResponseStatus(HttpStatus.OK)' + newline +
    '    List<' + resourceClass + '>' + ' getAll' + resources.capitalize() + '() { ' + newline +
    '        return ' + serviceInstance + '.getAll' + resources.capitalize() + '();' + newline +
    '    }' + newline +
    newline +
    '    @RequestMapping(value = "", method = RequestMethod.POST)' + newline +
    '    @ResponseStatus(HttpStatus.CREATED)' + newline +
    '    ' + resourceClass + ' create' + resourceClass + '(@RequestBody @Validated(' + resourceClass + '.Create.class) ' + resourceClass + ' ' + resourceInstance + ') { ' + newline +
    '        return ' + serviceInstance + '.create' + resourceClass + '(' + resourceInstance + ');' + newline +
    '    }' + newline +
    newline +
    '    @RequestMapping(value = "", method = RequestMethod.PUT)' + newline +
    '    @ResponseStatus(HttpStatus.OK)' + newline +
    '    ' + resourceClass + ' update' + resourceClass + '(@RequestBody @Validated(' + resourceClass + '.Update.class) ' + resourceClass + ' ' + resourceInstance + ') throws ' + serviceClass + '.NotFoundException { ' + newline +
    '        return ' + serviceInstance + '.update' + resourceClass + '(' + resourceInstance + ');' + newline +
    '    }' + newline +
    newline +
    '    @RequestMapping("/{id}")' + newline +
    '    @ResponseStatus(HttpStatus.OK)' + newline +
    '    ' + resourceClass + ' get' + resourceClass + 'ById(@PathVariable("id") ' + idClass + ' id) throws ' + serviceClass + '.NotFoundException { ' + newline +
    '        return ' + serviceInstance + '.get' + resourceClass + 'ById(id);' + newline +
    '    }' + newline +
    newline +
    '    @RequestMapping(value = "/{id}", method = RequestMethod.DELETE)' + newline +
    '    @ResponseStatus(HttpStatus.NO_CONTENT)' + newline +
    '    void delete' + resourceClass + '(@PathVariable("id") ' + idClass + ' id) throws ' + serviceClass + '.NotFoundException {' + newline +
    '        ' + serviceInstance + '.softDelete' + resourceClass + 'ById(id);' + newline +
    '    }' + newline +
    newline +
    '    @ExceptionHandler(' + serviceClass + '.NotFoundException.class)' + newline +
    '    @ResponseStatus(HttpStatus.NOT_FOUND)' + newline +
    '    Map handleNotFoundException(HttpServletRequest request, ' + serviceClass + '.NotFoundException ex) {' + newline +
    '        Map<String, String> map = new LinkedHashMap<>();' + newline +
    '        map.put("timestamp", new Date().toInstant().atOffset(ZoneOffset.UTC).format(DateTimeFormatter.ofPattern("yyyy\'-\'mm\'-\'dd\'T\'kk\'-\'mm\'-\'ss\'.\'SSSxxxx")));' + newline +
    '        map.put("status", "404");' + newline +
    '        map.put("error", "Not Found");' + newline +
    '        map.put("message", "Was unable to locate an item with the id: " + ex.getId().toString());' + newline +
    '        map.put("path", request.getServletPath());' + newline +
    '        return map;' + newline +
    '    }' + newline +
    newline +
    '}'
    )
    file.close()

def createResourceClass(directory, packagePrefix, resourceName, idClass, newline, customPackage):
    file = open(directory + resourceName.capitalize() +'.java', 'w+')
    resourceClass = resourceName.capitalize()
    file.writelines(
    'package ' + packagePrefix + '.' + resourceName.lower() + 's;' + newline +
    newline +
    (('import ' + customPackage + '.' + idClass + newline + newline) if customPackage else ('')) +
    'import com.fasterxml.jackson.annotation.JsonIgnore;' + newline +
    newline +
    'import javax.persistence.Entity;' + newline +
    'import javax.persistence.GeneratedValue;' + newline +
    'import javax.persistence.Id;' + newline +
    'import javax.validation.constraints.NotNull;' + newline +
    'import javax.validation.constraints.Null;' + newline +
    newline +
    '@Entity' + newline +
    'public class ' + resourceClass + ' {' + newline +
    '    @Id' + newline +
    '    @GeneratedValue' + newline +
    '    @Null(groups = Create.class)' + newline +
    '    @NotNull(groups = Update.class)' + newline +
    '    private ' + idClass + ' id;' + newline +
    newline +
    '    @JsonIgnore' + newline +
    '    @Null(groups = {Create.class, Update.class})' + newline +
    '    private Boolean deleted;' + newline +
    newline +
    '    @Null(groups = Create.class)' + newline +
    '    private Long createdAt;' + newline +
    newline +
    '    @Null(groups = Create.class)' + newline +
    '    private Long updatedAt;' + newline +
    newline +
    '    public ' + idClass + ' getId() {' + newline +
    '        return id;' + newline +
    '    }' + newline +
    newline +
    '    public void setId(' + idClass+' id) {' + newline +
    '        this.id = id;' + newline + 
    '    }' + newline +
    newline+
    '    public Boolean isDeleted() {' + newline +
    '        return deleted;' + newline +
    '    }' + newline +
    newline +
    '    public void setDeleted(Boolean deleted) {' + newline +
    '        this.deleted = deleted;' + newline +
    '    }' + newline +
    newline +
    '    public Long getCreatedAt() {' + newline +
    '        return createdAt;' + newline +
    '    }' + newline +
    newline +
    '    public void setCreatedAt(Long createdAt) {' + newline +
    '        this.createdAt = createdAt;' + newline +
    '    }' + newline +
    newline+
    '    public Long getUpdatedAt() {' + newline +
    '        return updatedAt;' + newline +
    '    }' + newline +
    newline +
    '    public void setUpdatedAt(Long updatedAt) {' + newline +
    '        this.updatedAt = updatedAt;' + newline +
    '    }' + newline +
    newline +
    '    interface Create { }' + newline +
    '    interface Update { }' + newline +
    '}'
    )
    file.close()

def createServiceClass(directory, packagePrefix, resourceName, idClass, newline, customPackage):
    file = open(directory + resourceName.capitalize()+'Service.java', 'w+')
    resourceClass = resourceName.capitalize()
    resourceInstance = resourceName[0:1].lower() + resourceName[1:]
    serviceClass = resourceName.capitalize() + 'Service'
    repositoryClass = resourceName.capitalize()+'Repository'
    repositoryInstance = resourceName[0:1].lower() + resourceName[1:] + 'Repository'
    file.writelines(
    'package ' + packagePrefix + '.' + resourceName.lower() + 's;' + newline +
    newline +
    (('import ' + customPackage + '.' + idClass + newline + newline) if customPackage else ('')) +
    'import org.springframework.beans.factory.annotation.Autowired;' + newline +
    'import org.springframework.stereotype.Service;' + newline +
    newline +
    'import java.util.List;' + newline +
    newline +
    '@Service' + newline +
    'public class ' + serviceClass + ' {' + newline +
    newline +
    '    private ' + repositoryClass + ' ' + repositoryInstance + ';' + newline +
    newline +
    '    @Autowired' + newline +
    '    public ' + serviceClass + '(' + repositoryClass + ' ' + repositoryInstance + ') {' + newline +
    '        this.' + repositoryInstance + ' = ' + repositoryInstance + ';' + newline +
    '    }' + newline +
    newline +
    '    public List<' + resourceClass + '> getAll' + resourceClass + 's() {' + newline +
    '        return ' + repositoryInstance + '.findAllByDeletedIsFalse();' + newline +
    '    }' + newline +
    newline +
    '    public ' + resourceClass + ' create' + resourceClass + '(' + resourceClass + ' ' + resourceInstance + ') {' + newline +
    '        long creationTime = System.currentTimeMillis();' + newline +
    '        ' + resourceInstance + '.setDeleted(false);' + newline +
    '        ' + resourceInstance + '.setCreatedAt(creationTime);' + newline +
    '        ' + resourceInstance + '.setUpdatedAt(creationTime);' + newline +
    '        return ' + repositoryInstance + '.save(' + resourceInstance + ');' + newline +
    '    }' + newline +
    newline +
    '    public ' + resourceClass + ' update' + resourceClass + '(' + resourceClass + ' ' + resourceInstance + ') throws NotFoundException {' + newline +
    '        ' + resourceClass + ' saved = get' + resourceClass + 'ById(' + resourceInstance + '.getId());' + newline +
    '        saved.setUpdatedAt(System.currentTimeMillis());' + newline +
    '        return ' + repositoryInstance + '.save(saved);' + newline +
    '    }' + newline +
    newline +
    '    public ' + resourceClass + ' get' + resourceClass + 'ById(' + idClass + ' id) throws NotFoundException {' + newline +
    '        return ' + repositoryInstance + '.findByIdAndDeletedIsFalse(id).orElseThrow(() -> new NotFoundException(id));' + newline +
    '    }' + newline +
    newline +
    '    public void softDelete' + resourceClass + 'ById(' + idClass + ' id) throws NotFoundException {' + newline +
    '        ' + resourceClass + ' ' + resourceInstance + 'ById = get' + resourceClass + 'ById(id);' + newline +
    '        ' + resourceInstance + 'ById.setDeleted(true);' + newline +
    '        ' + repositoryInstance + '.save(' + resourceInstance + 'ById);' + newline +
    '    }' + newline +
    newline +
    '    static class NotFoundException extends Exception {' + newline +
    '        private ' + idClass + ' id;' + newline +
    newline +
    '        NotFoundException(' +idClass + ' id) {' + newline +
    '            this.id = id;' + newline +
    '        }' + newline +
    newline +
    '        public ' + idClass + ' getId() {' + newline +
    '            return id;' + newline +
    '        }' + newline +
    '    }' + newline +
    '}'
    )
    file.close()

def createRepositoryClass(directory, packagePrefix, resourceName, idClass, newline, customPackage):
    file = open(directory + resourceName.capitalize()+'Repository.java', 'w+')
    resourceClass = resourceName.capitalize()
    repositoryClass = resourceName.capitalize()+'Repository'
    file.writelines(
    'package ' + packagePrefix + '.' + resourceName.lower() + 's;' + newline +
    newline +
    (('import ' + customPackage + '.' + idClass + newline + newline) if customPackage else ('')) +
    'import org.springframework.data.repository.CrudRepository;' + newline +
    'import org.springframework.stereotype.Repository;' + newline +
    newline +
    'import java.util.List;' + newline +
    'import java.util.Optional;' + newline +
    newline +
    '@Repository' + newline +
    'public interface ' + repositoryClass + ' extends CrudRepository<' + resourceClass + ', ' + idClass + '> {' + newline +
    '    List<' + resourceClass + '> findAllByDeletedIsFalse();' + newline +
    newline +
    '    Optional<' + resourceClass + '> findByIdAndDeletedIsFalse(' + idClass + ' id);' + newline +
    '}'
    )
    file.close()


def run():
    cwd = os.getcwd()
    directory = input('Enter directory to generate package: (default '+ cwd+') ')
    if (len(directory) == 0):
        directory = cwd
    if not os.path.isdir(directory):
        if directory[0] != slash:
            directory = cwd + (slash if cwd[-1] != slash else '') + directory
        else:
            directory = (cwd[:-1] if cwd[-1] == slash else cwd) + directory
        print(directory)
        if not os.path.isdir(directory):
            print('Invalid directory')
            return
    if directory[:-1] != slash:
        directory += slash
    packagePrefix = input('Enter full prefix for package name: (ex: com.ianswift.rest) ')
    resourceName = input('Enter singular name of the resource: (ex: Item) ')
    idClass = input('Enter class for resource id: (default Integer) ')
    customPackage = False
    if idClass == '':
        idClass = 'Integer'
    elif idClass not in ['Boolean', 'Byte', 'Character', 'Double', 'Float', 'Integer', 'Long', 'Number', 'Object', 'Short', 'String']:
        customPackage = input('Custom class detected! If class is from java.lang press enter to skip. Otherwise, enter package name: ')
        customPackage = customPackage if customPackage != '' else False
    newline = input('Use Windows newlines? (default no): ')
    while (newline not in ['Y','y','YES','yes', 'N', 'n', 'NO', 'no', '']):
        newline = input('Please enter yes or no: ')
    if (newline in ['Y', 'y', 'YES', 'yes']):
        newline = '\r\n'
    else:
        newline = '\n'

    directory = createRootDirectory(directory, resourceName) + slash
    createControllerClass(directory, packagePrefix, resourceName, idClass, newline, customPackage)
    createResourceClass(directory, packagePrefix, resourceName, idClass, newline, customPackage)
    createServiceClass(directory, packagePrefix, resourceName, idClass, newline, customPackage)
    createRepositoryClass(directory, packagePrefix, resourceName, idClass, newline, customPackage)
run()
